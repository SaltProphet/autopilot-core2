"""Content & Asset Generator Engine"""

import shutil
from pathlib import Path
from typing import Dict, List

from pi_core.models import Product, ProductType


class ContentGeneratorEngine:
    """Engine for generating content and assets for products"""

    def __init__(self, artifacts_dir: Path):
        self.artifacts_dir = artifacts_dir

    async def generate_assets(self, product: Product) -> Path:
        """Generate all assets for a product"""
        product_dir = self.artifacts_dir / product.id
        product_dir.mkdir(parents=True, exist_ok=True)

        # Generate README
        await self._generate_readme(product, product_dir)

        # Generate type-specific assets
        if product.product_type == ProductType.SCRIPT:
            await self._generate_script_assets(product, product_dir)
        elif product.product_type == ProductType.MICRO_TOOL:
            await self._generate_tool_assets(product, product_dir)
        elif product.product_type == ProductType.GUIDE:
            await self._generate_guide_assets(product, product_dir)
        elif product.product_type == ProductType.TEMPLATE:
            await self._generate_template_assets(product, product_dir)

        # Generate usage instructions
        await self._generate_usage_instructions(product, product_dir)

        return product_dir

    async def _generate_readme(self, product: Product, product_dir: Path):
        """Generate README file"""
        readme_content = f"""# {product.title}

## Overview

{product.value_proposition}

## Target Audience

{product.target_persona}

## Features

{self._format_list(product.features)}

## What This Is NOT

{self._format_list(product.non_goals)}

## Why This is Shippable

{product.why_shippable}

## Quick Start

See `USAGE.md` for detailed instructions.

## License

MIT License - Use freely in your projects.
"""
        (product_dir / "README.md").write_text(readme_content)

    async def _generate_usage_instructions(self, product: Product, product_dir: Path):
        """Generate usage instructions"""
        usage_content = f"""# Usage Instructions - {product.title}

## Installation

"""
        if product.product_type == ProductType.SCRIPT:
            usage_content += """1. Download the script file
2. Make it executable: `chmod +x script.py`
3. Run: `./script.py`

## Configuration

Edit the configuration section at the top of the script to customize behavior.

## Examples

```bash
# Basic usage
./script.py

# With options
./script.py --option value
```
"""
        elif product.product_type == ProductType.MICRO_TOOL:
            usage_content += """1. Download and extract the tool
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## Usage

Launch the tool and follow the on-screen instructions.
"""
        elif product.product_type == ProductType.GUIDE:
            usage_content += """This is a guide document. Read through the sections in order.

## Navigation

- Start with `01-introduction.md`
- Follow the numbered sections
- Reference `troubleshooting.md` if you encounter issues
"""
        elif product.product_type == ProductType.TEMPLATE:
            usage_content += """1. Copy the template files to your project
2. Customize the configuration files
3. Follow the integration guide

## Customization

Edit the provided files to match your requirements.
"""

        (product_dir / "USAGE.md").write_text(usage_content)

    async def _generate_script_assets(self, product: Product, product_dir: Path):
        """Generate script assets"""
        script_content = f"""#!/usr/bin/env python3
\"\"\"
{product.title}

{product.value_proposition}
\"\"\"

import argparse
import sys


def main():
    \"\"\"Main entry point\"\"\"
    parser = argparse.ArgumentParser(
        description="{product.title}"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        print("Running in verbose mode...")
    
    # TODO: Implement core functionality
    print("Script executed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
"""
        (product_dir / "script.py").write_text(script_content)
        (product_dir / "script.py").chmod(0o755)

    async def _generate_tool_assets(self, product: Product, product_dir: Path):
        """Generate micro-tool assets"""
        # Main application file
        main_content = f"""#!/usr/bin/env python3
\"\"\"
{product.title}

{product.value_proposition}
\"\"\"


def main():
    \"\"\"Main application entry point\"\"\"
    print("="* 50)
    print(f"{product.title}")
    print("="* 50)
    print()
    
    # TODO: Implement core functionality
    
    print("\\nOperation completed successfully!")


if __name__ == "__main__":
    main()
"""
        (product_dir / "main.py").write_text(main_content)

        # Requirements file
        requirements = "# Add required dependencies here\n"
        (product_dir / "requirements.txt").write_text(requirements)

    async def _generate_guide_assets(self, product: Product, product_dir: Path):
        """Generate guide assets"""
        intro_content = f"""# Introduction - {product.title}

## What You'll Learn

{product.value_proposition}

## Prerequisites

- Basic understanding of the problem domain
- Access to necessary tools/software

## Structure

This guide is organized into the following sections:

{self._format_numbered_list([f.replace("Step-by-step ", "") for f in product.features[:3]])}
"""
        (product_dir / "01-introduction.md").write_text(intro_content)

        steps_content = """# Step-by-Step Instructions

## Step 1: Setup

1. First action
2. Second action
3. Third action

## Step 2: Implementation

1. First action
2. Second action
3. Third action

## Step 3: Verification

1. Test your implementation
2. Verify the results
"""
        (product_dir / "02-steps.md").write_text(steps_content)

        troubleshooting_content = """# Troubleshooting

## Common Issues

### Issue 1: [Problem Description]

**Symptoms:**
- Symptom 1
- Symptom 2

**Solution:**
1. Step 1
2. Step 2

### Issue 2: [Problem Description]

**Symptoms:**
- Symptom 1

**Solution:**
1. Step 1
"""
        (product_dir / "troubleshooting.md").write_text(troubleshooting_content)

    async def _generate_template_assets(self, product: Product, product_dir: Path):
        """Generate template assets"""
        # Template structure
        template_dir = product_dir / "template"
        template_dir.mkdir(exist_ok=True)

        config_content = f"""# Configuration Template
# {product.title}

[settings]
option1 = value1
option2 = value2

[advanced]
# Advanced options
debug = false
"""
        (template_dir / "config.ini").write_text(config_content)

        integration_content = f"""# Integration Guide - {product.title}

## Quick Integration

1. Copy files from `template/` directory to your project
2. Update `config.ini` with your settings
3. Follow the usage examples below

## Usage Examples

Example 1: Basic usage
Example 2: Advanced usage
"""
        (product_dir / "INTEGRATION.md").write_text(integration_content)

    def _format_list(self, items: List[str]) -> str:
        """Format a list of items as markdown"""
        return "\n".join(f"- {item}" for item in items)

    def _format_numbered_list(self, items: List[str]) -> str:
        """Format a numbered list as markdown"""
        return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
