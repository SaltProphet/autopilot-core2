"""Marketplace Packaging Engine"""

import shutil
import zipfile
from pathlib import Path
from typing import List, Tuple

from pi_core.models import Product, MarketplaceListing


class MarketplacePackagingEngine:
    """Engine for packaging products for marketplace listing"""

    def __init__(self, artifacts_dir: Path):
        self.artifacts_dir = artifacts_dir

    async def create_listing(self, product: Product, product_dir: Path) -> MarketplaceListing:
        """Create a marketplace listing for a product"""
        
        # Generate listing details
        title = self._generate_listing_title(product)
        title_variants = self._generate_title_variants(product)
        description = self._generate_description(product)
        feature_bullets = self._generate_feature_bullets(product)
        faq = self._generate_faq(product)
        anchor_price, impulse_price = self._suggest_pricing(product)
        
        # Create asset bundle
        bundle_path = await self._create_asset_bundle(product, product_dir)

        return MarketplaceListing(
            product_id=product.id,
            title=title,
            title_variants=title_variants,
            description=description,
            feature_bullets=feature_bullets,
            faq=faq,
            anchor_price=anchor_price,
            impulse_price=impulse_price,
            asset_bundle_path=str(bundle_path),
        )

    def _generate_listing_title(self, product: Product) -> str:
        """Generate main marketplace title"""
        # Keep it under 60 characters for marketplaces
        base_title = product.title[:50]
        
        if product.product_type.value == "script":
            suffix = " - Automation Script"
        elif product.product_type.value == "micro_tool":
            suffix = " - Quick Tool"
        elif product.product_type.value == "guide":
            suffix = " - Complete Guide"
        else:  # template
            suffix = " - Ready Template"
        
        full_title = base_title + suffix
        return full_title[:60]

    def _generate_title_variants(self, product: Product) -> List[str]:
        """Generate alternative title options"""
        base = product.title[:40]
        variants = []
        
        if product.product_type.value == "script":
            variants = [
                f"{base} - Automate Your Workflow",
                f"Easy {base} Automation",
                f"{base} Script - Time Saver",
            ]
        elif product.product_type.value == "micro_tool":
            variants = [
                f"{base} - Simple Solution",
                f"Quick {base} Tool",
                f"{base} - No Setup Required",
            ]
        elif product.product_type.value == "guide":
            variants = [
                f"Master {base} - Step-by-Step",
                f"{base} - Complete Tutorial",
                f"Learn {base} Fast",
            ]
        else:  # template
            variants = [
                f"{base} - Plug & Play Template",
                f"Ready-Made {base}",
                f"{base} Template - Just Customize",
            ]
        
        return [v[:60] for v in variants]

    def _generate_description(self, product: Product) -> str:
        """Generate marketplace description"""
        description = f"""## What You Get

{product.value_proposition}

## Why This Product?

{product.why_shippable}

## Features

{self._format_features(product.features)}

## Perfect For

{product.target_persona}

## What's Included

- Complete source code/content
- Detailed usage instructions
- Ready to use immediately
- No ongoing costs or subscriptions

## Not Included

{self._format_features(product.non_goals)}

## Instant Download

Purchase once, use forever. No DRM, no restrictions.
"""
        return description

    def _generate_feature_bullets(self, product: Product) -> List[str]:
        """Generate feature bullet points for marketplace"""
        bullets = [
            f"✓ {product.value_proposition}",
            "✓ Instant download - start using immediately",
            "✓ Complete documentation included",
        ]
        
        # Add top 3 features
        for feature in product.features[:3]:
            bullets.append(f"✓ {feature}")
        
        bullets.append("✓ No subscription or ongoing fees")
        
        return bullets

    def _generate_faq(self, product: Product) -> List[dict]:
        """Generate FAQ section"""
        faq = [
            {
                "question": "What exactly do I get?",
                "answer": f"You get all the files needed to use this {product.product_type.value}, "
                          f"including complete documentation and usage instructions."
            },
            {
                "question": "Is this a one-time purchase?",
                "answer": "Yes! Purchase once and use forever. No subscriptions or recurring fees."
            },
            {
                "question": "Do I need special software?",
                "answer": "Minimal requirements. Details are in the product documentation."
            },
            {
                "question": "Can I customize it?",
                "answer": "Absolutely! All source code/content is included and can be modified to fit your needs."
            },
            {
                "question": "Do you offer support?",
                "answer": "The product includes comprehensive documentation. For additional questions, "
                          "contact via the marketplace messaging system."
            },
        ]
        
        return faq

    def _suggest_pricing(self, product: Product) -> Tuple[float, float]:
        """Suggest pricing for the product"""
        # Base pricing on product type
        if product.product_type.value == "guide":
            anchor = 29.99
            impulse = 19.99
        elif product.product_type.value == "template":
            anchor = 39.99
            impulse = 24.99
        elif product.product_type.value == "script":
            anchor = 34.99
            impulse = 19.99
        else:  # micro_tool
            anchor = 49.99
            impulse = 29.99
        
        return anchor, impulse

    async def _create_asset_bundle(self, product: Product, product_dir: Path) -> Path:
        """Create a ZIP bundle of all product assets"""
        bundle_name = f"{product.id}.zip"
        bundle_path = self.artifacts_dir / bundle_name
        
        # Create ZIP file
        with zipfile.ZipFile(bundle_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in product_dir.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(product_dir)
                    zipf.write(file_path, arcname)
        
        return bundle_path

    def _format_features(self, items: List[str]) -> str:
        """Format items as bullet points"""
        return "\n".join(f"- {item}" for item in items)
