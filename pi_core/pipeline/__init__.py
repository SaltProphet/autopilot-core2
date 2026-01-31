"""Pipeline orchestration and execution"""

import asyncio
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from pi_core.config import config
from pi_core.database import Database
from pi_core.engines import ProblemDiscoveryEngine
from pi_core.engines.product_definition import ProductDefinitionEngine
from pi_core.engines.content_generator import ContentGeneratorEngine
from pi_core.engines.marketplace_packaging import MarketplacePackagingEngine
from pi_core.models import (
    PipelineRun,
    PipelineStage,
    PipelineStatus,
    Problem,
    Product,
    MarketplaceListing,
)


class PipelineRunner:
    """Orchestrates the end-to-end pipeline execution"""

    def __init__(self, db: Database):
        self.db = db
        self.config = config
        
        # Initialize engines
        self.discovery_engine = ProblemDiscoveryEngine()
        self.definition_engine = ProductDefinitionEngine()
        self.content_engine = ContentGeneratorEngine(config.pipeline.artifacts_dir)
        self.packaging_engine = MarketplacePackagingEngine(config.pipeline.artifacts_dir)
        
        # Current run tracking
        self.current_run: Optional[PipelineRun] = None

    async def run_full_pipeline(
        self,
        problem_id: Optional[str] = None,
        start_from: PipelineStage = PipelineStage.DISCOVER,
    ) -> PipelineRun:
        """
        Run the full pipeline from discovery to packaging
        
        Args:
            problem_id: Optional specific problem ID to process (skips discovery)
            start_from: Pipeline stage to start from
            
        Returns:
            PipelineRun with execution details
        """
        # Create new pipeline run
        self.current_run = PipelineRun(
            stage=start_from,
            status=PipelineStatus.RUNNING,
        )
        self.db.save_pipeline_run(self.current_run)
        
        try:
            # Stage 1: Discover
            if start_from == PipelineStage.DISCOVER:
                problem = await self._run_discover_stage()
                if not problem:
                    return await self._fail_run("No problems discovered")
                self.current_run.problem_id = problem.id
            else:
                # Load existing problem
                if not problem_id:
                    return await self._fail_run("Problem ID required when skipping discovery")
                problem = self.db.get_problem(problem_id)
                if not problem:
                    return await self._fail_run(f"Problem {problem_id} not found")
                self.current_run.problem_id = problem.id
            
            # Stage 2: Define
            if start_from.value in [s.value for s in [PipelineStage.DISCOVER, PipelineStage.DEFINE]]:
                product = await self._run_define_stage(problem)
                if not product:
                    return await self._fail_run("Failed to define product")
                self.current_run.product_id = product.id
            
            # Stage 3: Build
            if start_from.value in [s.value for s in [
                PipelineStage.DISCOVER, 
                PipelineStage.DEFINE, 
                PipelineStage.BUILD
            ]]:
                # Get the product if we don't have it from previous stage
                if 'product' not in locals():
                    products = self.db.get_products(limit=1)
                    if not products:
                        return await self._fail_run("No product found to build")
                    product = products[0]
                
                product_dir = await self._run_build_stage(product)
                if not product_dir:
                    return await self._fail_run("Failed to build product")
                self.current_run.artifacts.append(str(product_dir))
            
            # Stage 4: Package
            if start_from.value in [s.value for s in [
                PipelineStage.DISCOVER, 
                PipelineStage.DEFINE, 
                PipelineStage.BUILD,
                PipelineStage.PACKAGE
            ]]:
                product_dir = Path(self.current_run.artifacts[-1]) if self.current_run.artifacts else None
                if not product_dir:
                    return await self._fail_run("No product artifacts found")
                
                listing = await self._run_package_stage(product, product_dir)
                if not listing:
                    return await self._fail_run("Failed to package product")
                self.current_run.listing_id = listing.id
            
            # Success!
            return await self._complete_run()
            
        except Exception as e:
            return await self._fail_run(f"Pipeline error: {str(e)}")

    async def _run_discover_stage(self) -> Optional[Problem]:
        """Run the discovery stage"""
        self._log("Starting discovery stage...")
        self.current_run.stage = PipelineStage.DISCOVER
        self.db.update_pipeline_run(self.current_run)
        
        try:
            problems = await self.discovery_engine.discover(limit=10)
            if not problems:
                self._log("No problems discovered")
                return None
            
            # Select top problem
            problem = problems[0]
            self.db.save_problem(problem)
            
            self._log(f"Discovered problem: {problem.title}")
            self._log(f"Confidence: {problem.confidence_score:.2f}, "
                     f"Frequency: {problem.frequency_score}, "
                     f"Recency: {problem.recency_score:.2f}")
            
            return problem
            
        except Exception as e:
            self._log(f"Discovery stage error: {e}")
            raise

    async def _run_define_stage(self, problem: Problem) -> Optional[Product]:
        """Run the product definition stage"""
        self._log("Starting definition stage...")
        self.current_run.stage = PipelineStage.DEFINE
        self.db.update_pipeline_run(self.current_run)
        
        try:
            product = await self.definition_engine.define_product(problem)
            self.db.save_product(product)
            
            self._log(f"Defined product: {product.title}")
            self._log(f"Type: {product.product_type.value}")
            self._log(f"Features: {len(product.features)}")
            
            return product
            
        except Exception as e:
            self._log(f"Definition stage error: {e}")
            raise

    async def _run_build_stage(self, product: Product) -> Optional[Path]:
        """Run the content generation stage"""
        self._log("Starting build stage...")
        self.current_run.stage = PipelineStage.BUILD
        self.db.update_pipeline_run(self.current_run)
        
        try:
            product_dir = await self.content_engine.generate_assets(product)
            
            self._log(f"Generated assets in: {product_dir}")
            self._log(f"Files created: {len(list(product_dir.rglob('*')))}")
            
            return product_dir
            
        except Exception as e:
            self._log(f"Build stage error: {e}")
            raise

    async def _run_package_stage(
        self, 
        product: Product, 
        product_dir: Path
    ) -> Optional[MarketplaceListing]:
        """Run the marketplace packaging stage"""
        self._log("Starting packaging stage...")
        self.current_run.stage = PipelineStage.PACKAGE
        self.db.update_pipeline_run(self.current_run)
        
        try:
            listing = await self.packaging_engine.create_listing(product, product_dir)
            self.db.save_listing(listing)
            
            self._log(f"Created marketplace listing: {listing.title}")
            self._log(f"Pricing: ${listing.impulse_price} (impulse) / ${listing.anchor_price} (anchor)")
            self._log(f"Bundle: {listing.asset_bundle_path}")
            
            return listing
            
        except Exception as e:
            self._log(f"Packaging stage error: {e}")
            raise

    async def _complete_run(self) -> PipelineRun:
        """Mark the run as completed"""
        self.current_run.status = PipelineStatus.SUCCESS
        self.current_run.completed_at = datetime.now(timezone.utc)
        self._log("Pipeline completed successfully!")
        self.db.update_pipeline_run(self.current_run)
        return self.current_run

    async def _fail_run(self, error_message: str) -> PipelineRun:
        """Mark the run as failed"""
        self.current_run.status = PipelineStatus.FAILED
        self.current_run.error_message = error_message
        self.current_run.completed_at = datetime.now(timezone.utc)
        self._log(f"Pipeline failed: {error_message}")
        self.db.update_pipeline_run(self.current_run)
        return self.current_run

    def _log(self, message: str):
        """Add a log message to the current run"""
        timestamp = datetime.now(timezone.utc).isoformat()
        log_entry = f"[{timestamp}] {message}"
        self.current_run.logs.append(log_entry)
        print(log_entry)  # Also print to console
