"""Configuration management for pi-core"""

import os
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class RedditConfig(BaseModel):
    """Reddit API configuration"""

    enabled: bool = True
    client_id: Optional[str] = Field(default_factory=lambda: os.getenv("REDDIT_CLIENT_ID"))
    client_secret: Optional[str] = Field(
        default_factory=lambda: os.getenv("REDDIT_CLIENT_SECRET")
    )
    user_agent: str = "pi-core/0.1.0"
    max_posts_per_run: int = 100


class GitHubConfig(BaseModel):
    """GitHub API configuration"""

    enabled: bool = True
    token: Optional[str] = Field(default_factory=lambda: os.getenv("GITHUB_TOKEN"))
    max_issues_per_run: int = 100


class GuardrailsConfig(BaseModel):
    """System guardrails configuration"""

    max_products_per_day: int = 5
    require_manual_approval: bool = True
    global_enabled: bool = True


class PipelineConfig(BaseModel):
    """Pipeline execution configuration"""

    data_dir: Path = Field(default_factory=lambda: Path("./data"))
    logs_dir: Path = Field(default_factory=lambda: Path("./logs"))
    artifacts_dir: Path = Field(default_factory=lambda: Path("./artifacts"))


class Config(BaseModel):
    """Main application configuration"""

    reddit: RedditConfig = Field(default_factory=RedditConfig)
    github: GitHubConfig = Field(default_factory=GitHubConfig)
    guardrails: GuardrailsConfig = Field(default_factory=GuardrailsConfig)
    pipeline: PipelineConfig = Field(default_factory=PipelineConfig)

    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        self.pipeline.data_dir.mkdir(parents=True, exist_ok=True)
        self.pipeline.logs_dir.mkdir(parents=True, exist_ok=True)
        self.pipeline.artifacts_dir.mkdir(parents=True, exist_ok=True)


# Global configuration instance
config = Config()
