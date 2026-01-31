"""Product Definition Engine"""

from typing import List

from pi_core.models import Problem, Product, ProductType, ProblemIntent


class ProductDefinitionEngine:
    """Engine for converting problems into product definitions"""

    async def define_product(self, problem: Problem) -> Product:
        """Define a product based on a problem"""
        
        # Determine product type based on problem characteristics
        product_type = self._determine_product_type(problem)
        
        # Generate target persona
        target_persona = self._generate_persona(problem)
        
        # Generate value proposition
        value_proposition = self._generate_value_prop(problem, product_type)
        
        # Generate features
        features = self._generate_features(problem, product_type)
        
        # Generate non-goals
        non_goals = self._generate_non_goals(product_type)
        
        # Why shippable
        why_shippable = self._generate_why_shippable(product_type)
        
        # Generate title
        title = self._generate_title(problem, product_type)

        return Product(
            problem_id=problem.id,
            title=title,
            product_type=product_type,
            target_persona=target_persona,
            value_proposition=value_proposition,
            features=features,
            non_goals=non_goals,
            why_shippable=why_shippable,
        )

    def _generate_title(self, problem: Problem, product_type: ProductType) -> str:
        """Generate product title"""
        # Clean up problem title
        base_title = problem.title.replace("How to ", "").replace("how to ", "")
        base_title = base_title[:50]  # Limit length
        
        # Add product type suffix
        if product_type == ProductType.SCRIPT:
            return f"{base_title} - Automation Script"
        elif product_type == ProductType.MICRO_TOOL:
            return f"{base_title} - Quick Tool"
        elif product_type == ProductType.GUIDE:
            return f"{base_title} - Complete Guide"
        else:  # TEMPLATE
            return f"{base_title} - Template"

    def _determine_product_type(self, problem: Problem) -> ProductType:
        """Determine the best product type for a problem"""
        keywords_lower = [k.lower() for k in problem.keywords]
        
        # Check for automation/script indicators
        if any(word in keywords_lower for word in ["automate", "script", "batch", "command"]):
            return ProductType.SCRIPT
        
        # Check for tool indicators
        if any(word in keywords_lower for word in ["tool", "utility", "app", "plugin"]):
            return ProductType.MICRO_TOOL
        
        # Check for guide/tutorial indicators
        if any(word in keywords_lower for word in ["learn", "tutorial", "guide", "how"]):
            return ProductType.GUIDE
        
        # Default to template for setup/configuration problems
        return ProductType.TEMPLATE

    def _generate_persona(self, problem: Problem) -> str:
        """Generate target user persona"""
        # Analyze problem source and keywords
        if problem.source.value == "github":
            return "Developers experiencing similar issues in their projects"
        elif problem.source.value == "reddit":
            if any(k in problem.keywords for k in ["beginner", "learning", "start"]):
                return "Beginner developers learning to code"
            else:
                return "Professional developers seeking solutions"
        else:
            return "Technical users facing similar challenges"

    def _generate_value_prop(self, problem: Problem, product_type: ProductType) -> str:
        """Generate value proposition"""
        problem_summary = problem.title[:50]
        
        if product_type == ProductType.SCRIPT:
            return f"Automates the solution to '{problem_summary}', saving hours of manual work."
        elif product_type == ProductType.MICRO_TOOL:
            return f"A simple tool that solves '{problem_summary}' with minimal setup."
        elif product_type == ProductType.GUIDE:
            return f"Step-by-step guide to resolve '{problem_summary}' permanently."
        else:  # TEMPLATE
            return f"Ready-to-use template that eliminates '{problem_summary}' from your workflow."

    def _generate_features(self, problem: Problem, product_type: ProductType) -> List[str]:
        """Generate feature checklist"""
        base_features = [
            "Solves the core problem directly",
            "Minimal setup required",
            "Clear documentation included",
        ]
        
        if product_type == ProductType.SCRIPT:
            base_features.extend([
                "Command-line interface",
                "Configurable options",
                "Error handling and logging",
            ])
        elif product_type == ProductType.MICRO_TOOL:
            base_features.extend([
                "Simple user interface",
                "Cross-platform compatibility",
                "Lightweight and fast",
            ])
        elif product_type == ProductType.GUIDE:
            base_features.extend([
                "Step-by-step instructions",
                "Screenshots and examples",
                "Troubleshooting section",
            ])
        else:  # TEMPLATE
            base_features.extend([
                "Ready-to-customize structure",
                "Best practices built-in",
                "Usage examples included",
            ])
        
        return base_features

    def _generate_non_goals(self, product_type: ProductType) -> List[str]:
        """Generate explicit non-goals"""
        return [
            "No enterprise-scale features",
            "No complex configuration",
            "No UI framework required",
            "No cloud infrastructure needed",
            "No ongoing maintenance burden",
        ]

    def _generate_why_shippable(self, product_type: ProductType) -> str:
        """Explain why this is small enough to ship"""
        if product_type == ProductType.SCRIPT:
            return "Single file script, under 200 lines, with clear inputs/outputs. Can be shipped in under 2 hours."
        elif product_type == ProductType.MICRO_TOOL:
            return "Focused on one task, minimal dependencies, basic UI. Shippable in 4-6 hours."
        elif product_type == ProductType.GUIDE:
            return "Documentation-only product. Core content can be written in 2-3 hours."
        else:  # TEMPLATE
            return "Pre-configured files and structure. Assembly and documentation in 2-3 hours."
