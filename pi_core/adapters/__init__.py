"""Adapter interfaces for extensibility"""

from abc import ABC, abstractmethod
from typing import List

from pi_core.models import Problem, Product, MarketplaceListing


class ProblemSourceAdapter(ABC):
    """Base adapter for problem sources"""

    @abstractmethod
    async def discover_problems(self, limit: int = 100) -> List[Problem]:
        """Discover problems from the source"""
        pass

    @abstractmethod
    def is_configured(self) -> bool:
        """Check if the adapter is properly configured"""
        pass


class ProductBuilderAdapter(ABC):
    """Base adapter for product builders"""

    @abstractmethod
    async def generate_product(self, problem: Problem) -> Product:
        """Generate a product from a problem"""
        pass


class MarketplaceAdapter(ABC):
    """Base adapter for marketplace integrations"""

    @abstractmethod
    async def create_listing(self, product: Product) -> MarketplaceListing:
        """Create a marketplace listing for a product"""
        pass

    @abstractmethod
    async def publish_listing(self, listing: MarketplaceListing) -> str:
        """Publish a listing to the marketplace, returns listing URL"""
        pass
