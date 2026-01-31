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
    updates = {}
    
    if patch.mode is not None:
        updates["mode"] = patch.mode
    if patch.max_cost_cents_per_run is not None:
        updates["max_cost_cents_per_run"] = patch.max_cost_cents_per_run
    if patch.banned_categories_json is not None:
        updates["banned_categories_json"] = patch.banned_categories_json
    if patch.hn_query is not None:
        updates["hn_query"] = patch.hn_query
    if patch.hn_limit is not None:
        updates["hn_limit"] = patch.hn_limit
    if patch.hn_tags is not None:
        updates["hn_tags"] = patch.hn_tags
    if patch.hn_by_date is not None:
        updates["hn_by_date"] = patch.hn_by_date
    
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
