"""Database management for pi-core"""

from pathlib import Path
from typing import List, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from pi_core.models import (
    Base,
    Problem,
    ProblemDB,
    Product,
    ProductDB,
    MarketplaceListing,
    MarketplaceListingDB,
    PipelineRun,
    PipelineRunDB,
)


class Database:
    """Database manager"""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        """Get a new database session"""
        return self.SessionLocal()

    def save_problem(self, problem: Problem) -> None:
        """Save a problem to the database"""
        session = self.get_session()
        try:
            db_problem = ProblemDB(
                id=problem.id,
                title=problem.title,
                description=problem.description,
                intent=problem.intent,
                source=problem.source,
                confidence_score=problem.confidence_score,
                frequency_score=problem.frequency_score,
                recency_score=problem.recency_score,
                evidence=[e.model_dump() for e in problem.evidence],
                keywords=problem.keywords,
                discovered_at=problem.discovered_at,
            )
            session.add(db_problem)
            session.commit()
        finally:
            session.close()

    def get_problems(self, limit: int = 100) -> List[Problem]:
        """Get all problems from the database"""
        session = self.get_session()
        try:
            db_problems = session.query(ProblemDB).order_by(
                ProblemDB.discovered_at.desc()
            ).limit(limit).all()
            
            from pi_core.models import EvidenceSnippet
            
            return [
                Problem(
                    id=p.id,
                    title=p.title,
                    description=p.description,
                    intent=p.intent,
                    source=p.source,
                    confidence_score=p.confidence_score,
                    frequency_score=p.frequency_score,
                    recency_score=p.recency_score,
                    evidence=[EvidenceSnippet(**e) for e in p.evidence],
                    keywords=p.keywords,
                    discovered_at=p.discovered_at,
                )
                for p in db_problems
            ]
        finally:
            session.close()

    def get_problem(self, problem_id: str) -> Optional[Problem]:
        """Get a specific problem by ID"""
        session = self.get_session()
        try:
            db_problem = session.query(ProblemDB).filter(ProblemDB.id == problem_id).first()
            if not db_problem:
                return None
            
            from pi_core.models import EvidenceSnippet
            
            return Problem(
                id=db_problem.id,
                title=db_problem.title,
                description=db_problem.description,
                intent=db_problem.intent,
                source=db_problem.source,
                confidence_score=db_problem.confidence_score,
                frequency_score=db_problem.frequency_score,
                recency_score=db_problem.recency_score,
                evidence=[EvidenceSnippet(**e) for e in db_problem.evidence],
                keywords=db_problem.keywords,
                discovered_at=db_problem.discovered_at,
            )
        finally:
            session.close()

    def save_product(self, product: Product) -> None:
        """Save a product to the database"""
        session = self.get_session()
        try:
            db_product = ProductDB(
                id=product.id,
                problem_id=product.problem_id,
                title=product.title,
                product_type=product.product_type,
                target_persona=product.target_persona,
                value_proposition=product.value_proposition,
                features=product.features,
                non_goals=product.non_goals,
                why_shippable=product.why_shippable,
                created_at=product.created_at,
            )
            session.add(db_product)
            session.commit()
        finally:
            session.close()

    def get_products(self, limit: int = 100) -> List[Product]:
        """Get all products from the database"""
        session = self.get_session()
        try:
            db_products = session.query(ProductDB).order_by(
                ProductDB.created_at.desc()
            ).limit(limit).all()
            
            return [
                Product(
                    id=p.id,
                    problem_id=p.problem_id,
                    title=p.title,
                    product_type=p.product_type,
                    target_persona=p.target_persona,
                    value_proposition=p.value_proposition,
                    features=p.features,
                    non_goals=p.non_goals,
                    why_shippable=p.why_shippable,
                    created_at=p.created_at,
                )
                for p in db_products
            ]
        finally:
            session.close()

    def save_listing(self, listing: MarketplaceListing) -> None:
        """Save a marketplace listing to the database"""
        session = self.get_session()
        try:
            db_listing = MarketplaceListingDB(
                id=listing.id,
                product_id=listing.product_id,
                title=listing.title,
                title_variants=listing.title_variants,
                description=listing.description,
                feature_bullets=listing.feature_bullets,
                faq=listing.faq,
                anchor_price=listing.anchor_price,
                impulse_price=listing.impulse_price,
                asset_bundle_path=listing.asset_bundle_path,
                created_at=listing.created_at,
            )
            session.add(db_listing)
            session.commit()
        finally:
            session.close()

    def get_listings(self, limit: int = 100) -> List[MarketplaceListing]:
        """Get all marketplace listings from the database"""
        session = self.get_session()
        try:
            db_listings = session.query(MarketplaceListingDB).order_by(
                MarketplaceListingDB.created_at.desc()
            ).limit(limit).all()
            
            return [
                MarketplaceListing(
                    id=l.id,
                    product_id=l.product_id,
                    title=l.title,
                    title_variants=l.title_variants,
                    description=l.description,
                    feature_bullets=l.feature_bullets,
                    faq=l.faq,
                    anchor_price=l.anchor_price,
                    impulse_price=l.impulse_price,
                    asset_bundle_path=l.asset_bundle_path,
                    created_at=l.created_at,
                )
                for l in db_listings
            ]
        finally:
            session.close()

    def save_pipeline_run(self, run: PipelineRun) -> None:
        """Save a pipeline run to the database"""
        session = self.get_session()
        try:
            db_run = PipelineRunDB(
                id=run.id,
                stage=run.stage,
                status=run.status,
                problem_id=run.problem_id,
                product_id=run.product_id,
                listing_id=run.listing_id,
                error_message=run.error_message,
                logs=run.logs,
                artifacts=run.artifacts,
                started_at=run.started_at,
                completed_at=run.completed_at,
            )
            session.add(db_run)
            session.commit()
        finally:
            session.close()

    def update_pipeline_run(self, run: PipelineRun) -> None:
        """Update an existing pipeline run"""
        session = self.get_session()
        try:
            db_run = session.query(PipelineRunDB).filter(PipelineRunDB.id == run.id).first()
            if db_run:
                db_run.stage = run.stage
                db_run.status = run.status
                db_run.problem_id = run.problem_id
                db_run.product_id = run.product_id
                db_run.listing_id = run.listing_id
                db_run.error_message = run.error_message
                db_run.logs = run.logs
                db_run.artifacts = run.artifacts
                db_run.completed_at = run.completed_at
                session.commit()
        finally:
            session.close()

    def get_pipeline_runs(self, limit: int = 100) -> List[PipelineRun]:
        """Get all pipeline runs from the database"""
        session = self.get_session()
        try:
            db_runs = session.query(PipelineRunDB).order_by(
                PipelineRunDB.started_at.desc()
            ).limit(limit).all()
            
            return [
                PipelineRun(
                    id=r.id,
                    stage=r.stage,
                    status=r.status,
                    problem_id=r.problem_id,
                    product_id=r.product_id,
                    listing_id=r.listing_id,
                    error_message=r.error_message,
                    logs=r.logs,
                    artifacts=r.artifacts,
                    started_at=r.started_at,
                    completed_at=r.completed_at,
                )
                for r in db_runs
            ]
        finally:
            session.close()

    def get_latest_run(self) -> Optional[PipelineRun]:
        """Get the most recent pipeline run"""
        runs = self.get_pipeline_runs(limit=1)
        return runs[0] if runs else None
