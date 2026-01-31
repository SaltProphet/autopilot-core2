"""Web UI for pi-core settings and control"""

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from core import settings

app = FastAPI(title="pi-core API", version="2.0.0")


class SettingsPatch(BaseModel):
    mode: Optional[str] = None
    max_cost_cents_per_run: Optional[int] = None
    banned_categories_json: Optional[str] = None
    hn_query: Optional[str] = None
    hn_limit: Optional[int] = None
    hn_tags: Optional[str] = None
    hn_by_date: Optional[str] = None


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "pi-core API",
        "version": "2.0.0",
        "description": "Hacker News problem discovery pipeline"
    }


@app.get("/api/settings")
async def get_settings():
    """Get current settings"""
    return settings.load_settings()


@app.patch("/api/settings")
async def update_settings(patch: SettingsPatch):
    """Update settings"""
    # Only include fields that were explicitly set
    updates = patch.model_dump(exclude_unset=True)
    
    settings.update(updates)
    
    return {
        "status": "success",
        "updated": list(updates.keys()),
        "current_settings": settings.load_settings()
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "2.0.0"}
