"""Data models for pi-core"""

from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field
from sqlalchemy import Column, DateTime, Enum as SQLEnum, Float, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Pydantic Models


class ProblemIntent(str, Enum):
    """Type of problem intent"""

    PAIN = "pain"
    WORKAROUND = "workaround"
    REQUEST = "request"


class ProblemSource(str, Enum):
    """Source of problem discovery"""

    REDDIT = "reddit"
    GITHUB = "github"
    STACKOVERFLOW = "stackoverflow"
    HACKERNEWS = "hackernews"


class ProductType(str, Enum):
    """Type of product to generate"""

    TEMPLATE = "template"
    SCRIPT = "script"
    GUIDE = "guide"
    MICRO_TOOL = "micro_tool"


class PipelineStage(str, Enum):
    """Pipeline execution stages"""

    DISCOVER = "discover"
    DEFINE = "define"
    BUILD = "build"
    PACKAGE = "package"
    PUBLISH = "publish"


class PipelineStatus(str, Enum):
    """Pipeline execution status"""

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"


class EvidenceSnippet(BaseModel):
    """Evidence snippet from a source"""

    text: str
    source_url: str
    author: Optional[str] = None
    timestamp: Optional[datetime] = None


class Problem(BaseModel):
    """Problem discovered from sources"""

    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: str
    intent: ProblemIntent
    source: ProblemSource
    confidence_score: float = Field(ge=0.0, le=1.0)
    frequency_score: int = Field(ge=0)
    recency_score: float = Field(ge=0.0, le=1.0)
    evidence: List[EvidenceSnippet] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)
    discovered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Product(BaseModel):
    """Product definition"""

    id: str = Field(default_factory=lambda: str(uuid4()))
    problem_id: str
    title: str
    product_type: ProductType
    target_persona: str
    value_proposition: str
    features: List[str] = Field(default_factory=list)
    non_goals: List[str] = Field(default_factory=list)
    why_shippable: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class MarketplaceListing(BaseModel):
    """Marketplace listing details"""

    id: str = Field(default_factory=lambda: str(uuid4()))
    product_id: str
    title: str
    title_variants: List[str] = Field(default_factory=list)
    description: str
    feature_bullets: List[str] = Field(default_factory=list)
    faq: List[dict] = Field(default_factory=list)
    anchor_price: float
    impulse_price: float
    asset_bundle_path: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PipelineRun(BaseModel):
    """Pipeline execution run"""

    id: str = Field(default_factory=lambda: str(uuid4()))
    stage: PipelineStage
    status: PipelineStatus
    problem_id: Optional[str] = None
    product_id: Optional[str] = None
    listing_id: Optional[str] = None
    error_message: Optional[str] = None
    logs: List[str] = Field(default_factory=list)
    artifacts: List[str] = Field(default_factory=list)
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None


# SQLAlchemy Models


class ProblemDB(Base):
    """Database model for problems"""

    __tablename__ = "problems"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    intent = Column(SQLEnum(ProblemIntent), nullable=False)
    source = Column(SQLEnum(ProblemSource), nullable=False)
    confidence_score = Column(Float, nullable=False)
    frequency_score = Column(Integer, nullable=False)
    recency_score = Column(Float, nullable=False)
    evidence = Column(JSON, nullable=False)
    keywords = Column(JSON, nullable=False)
    discovered_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class ProductDB(Base):
    """Database model for products"""

    __tablename__ = "products"

    id = Column(String, primary_key=True)
    problem_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    product_type = Column(SQLEnum(ProductType), nullable=False)
    target_persona = Column(String, nullable=False)
    value_proposition = Column(Text, nullable=False)
    features = Column(JSON, nullable=False)
    non_goals = Column(JSON, nullable=False)
    why_shippable = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class MarketplaceListingDB(Base):
    """Database model for marketplace listings"""

    __tablename__ = "marketplace_listings"

    id = Column(String, primary_key=True)
    product_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    title_variants = Column(JSON, nullable=False)
    description = Column(Text, nullable=False)
    feature_bullets = Column(JSON, nullable=False)
    faq = Column(JSON, nullable=False)
    anchor_price = Column(Float, nullable=False)
    impulse_price = Column(Float, nullable=False)
    asset_bundle_path = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class PipelineRunDB(Base):
    """Database model for pipeline runs"""

    __tablename__ = "pipeline_runs"

    id = Column(String, primary_key=True)
    stage = Column(SQLEnum(PipelineStage), nullable=False)
    status = Column(SQLEnum(PipelineStatus), nullable=False)
    problem_id = Column(String)
    product_id = Column(String)
    listing_id = Column(String)
    error_message = Column(Text)
    logs = Column(JSON, nullable=False)
    artifacts = Column(JSON, nullable=False)
    started_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    completed_at = Column(DateTime)
