#!/usr/bin/env python3
"""
Demo script to test pi-core pipeline with mock data

This demonstrates the complete pipeline without requiring API credentials.
"""

import asyncio
from datetime import datetime, timezone
from pathlib import Path

from pi_core.config import config
from pi_core.database import Database
from pi_core.models import (
    Problem,
    ProblemIntent,
    ProblemSource,
    EvidenceSnippet,
)
from pi_core.engines.product_definition import ProductDefinitionEngine
from pi_core.engines.content_generator import ContentGeneratorEngine
from pi_core.engines.marketplace_packaging import MarketplacePackagingEngine


async def demo_pipeline():
    """Run a demo pipeline with mock data"""
    print("🚀 Starting pi-core Demo Pipeline\n")
    
    # Setup
    config.ensure_directories()
    db = Database(config.pipeline.data_dir / "demo.db")
    
    # Create mock problem
    print("1️⃣ Creating mock problem...")
    problem = Problem(
        title="How to automate daily git commits",
        description="Many developers forget to commit their work daily. "
                    "Need an automated solution to remind and commit changes.",
        intent=ProblemIntent.PAIN,
        source=ProblemSource.REDDIT,
        confidence_score=0.85,
        frequency_score=42,
        recency_score=0.9,
        evidence=[
            EvidenceSnippet(
                text="I always forget to commit my work at end of day",
                source_url="https://reddit.com/r/programming/example",
                author="developer123",
                timestamp=datetime.now(timezone.utc),
            )
        ],
        keywords=["git", "commit", "automation", "daily", "reminder"],
    )
    
    db.save_problem(problem)
    print(f"   ✅ Problem created: {problem.title}")
    print(f"   📊 Confidence: {problem.confidence_score:.2f}, "
          f"Frequency: {problem.frequency_score}\n")
    
    # Define product
    print("2️⃣ Defining product...")
    definition_engine = ProductDefinitionEngine()
    product = await definition_engine.define_product(problem)
    db.save_product(product)
    print(f"   ✅ Product defined: {product.title}")
    print(f"   📦 Type: {product.product_type.value}")
    print(f"   💡 Value: {product.value_proposition}\n")
    
    # Generate content
    print("3️⃣ Generating content and assets...")
    content_engine = ContentGeneratorEngine(config.pipeline.artifacts_dir)
    product_dir = await content_engine.generate_assets(product)
    print(f"   ✅ Assets generated in: {product_dir}")
    
    # List generated files
    files = list(product_dir.rglob("*"))
    print(f"   📁 Files created: {len(files)}")
    for file in files[:5]:
        if file.is_file():
            print(f"      - {file.relative_to(product_dir)}")
    if len(files) > 5:
        print(f"      ... and {len(files) - 5} more files\n")
    else:
        print()
    
    # Package for marketplace
    print("4️⃣ Packaging for marketplace...")
    packaging_engine = MarketplacePackagingEngine(config.pipeline.artifacts_dir)
    listing = await packaging_engine.create_listing(product, product_dir)
    db.save_listing(listing)
    print(f"   ✅ Listing created: {listing.title}")
    print(f"   💰 Pricing: ${listing.impulse_price:.2f} (impulse) / "
          f"${listing.anchor_price:.2f} (anchor)")
    print(f"   📦 Bundle: {Path(listing.asset_bundle_path).name}\n")
    
    # Summary
    print("✨ Demo Pipeline Complete!\n")
    print("Summary:")
    print(f"  - Problem discovered: {problem.title}")
    print(f"  - Product created: {product.title} ({product.product_type.value})")
    print(f"  - Assets generated: {len(files)} files")
    print(f"  - Marketplace listing: Ready with pricing and bundle")
    print(f"\n📊 View results:")
    print(f"  - Database: {config.pipeline.data_dir / 'demo.db'}")
    print(f"  - Artifacts: {config.pipeline.artifacts_dir}")
    print(f"  - Product files: {product_dir}")
    print(f"\n🌐 Start the dashboard to view in UI:")
    print(f"  python main.py")


if __name__ == "__main__":
    asyncio.run(demo_pipeline())
