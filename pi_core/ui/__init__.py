"""Web UI for pi-core dashboard"""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pi_core.config import config
from pi_core.database import Database
from pi_core.pipeline import PipelineRunner
from pi_core.models import PipelineStage

# Initialize FastAPI app
app = FastAPI(title="pi-core Dashboard", version="0.1.0")

# Initialize database
config.ensure_directories()
db = Database(config.pipeline.data_dir / "pi_core.db")

# Initialize pipeline runner
pipeline_runner = PipelineRunner(db)

# Setup templates
templates_dir = Path(__file__).parent / "templates"
templates_dir.mkdir(exist_ok=True)
templates = Jinja2Templates(directory=str(templates_dir))


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard page"""
    # Get latest run
    latest_run = db.get_latest_run()
    
    # Get recent items
    problems = db.get_problems(limit=10)
    products = db.get_products(limit=10)
    listings = db.get_listings(limit=10)
    recent_runs = db.get_pipeline_runs(limit=10)
    
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "latest_run": latest_run,
            "problems": problems,
            "products": products,
            "listings": listings,
            "recent_runs": recent_runs,
            "config": config,
        },
    )


@app.get("/api/config")
async def get_config():
    """Get current configuration"""
    return {
        "reddit": {
            "enabled": config.reddit.enabled,
            "configured": config.reddit.client_id is not None,
        },
        "github": {
            "enabled": config.github.enabled,
            "configured": config.github.token is not None,
        },
        "guardrails": {
            "max_products_per_day": config.guardrails.max_products_per_day,
            "require_manual_approval": config.guardrails.require_manual_approval,
            "global_enabled": config.guardrails.global_enabled,
        },
    }


@app.post("/api/config/update")
async def update_config(updates: dict):
    """Update configuration"""
    if "reddit_enabled" in updates:
        config.reddit.enabled = updates["reddit_enabled"]
    if "github_enabled" in updates:
        config.github.enabled = updates["github_enabled"]
    if "guardrails_enabled" in updates:
        config.guardrails.global_enabled = updates["guardrails_enabled"]
    if "max_products_per_day" in updates:
        config.guardrails.max_products_per_day = updates["max_products_per_day"]
    if "require_approval" in updates:
        config.guardrails.require_manual_approval = updates["require_approval"]
    
    return {"status": "success"}


@app.post("/api/pipeline/run")
async def run_pipeline():
    """Start a new pipeline run"""
    if not config.guardrails.global_enabled:
        return JSONResponse(
            status_code=400,
            content={"error": "Pipeline is disabled via kill switch"}
        )
    
    try:
        run = await pipeline_runner.run_full_pipeline()
        return {
            "status": "success",
            "run_id": run.id,
            "final_status": run.status.value,
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.get("/api/pipeline/status")
async def pipeline_status():
    """Get current pipeline status"""
    latest_run = db.get_latest_run()
    
    if not latest_run:
        return {"status": "idle"}
    
    return {
        "status": latest_run.status.value,
        "stage": latest_run.stage.value,
        "started_at": latest_run.started_at.isoformat(),
        "logs": latest_run.logs[-10:],  # Last 10 log entries
    }


@app.get("/api/problems")
async def list_problems(limit: int = 100):
    """List discovered problems"""
    problems = db.get_problems(limit=limit)
    return [p.model_dump() for p in problems]


@app.get("/api/products")
async def list_products(limit: int = 100):
    """List generated products"""
    products = db.get_products(limit=limit)
    return [p.model_dump() for p in products]


@app.get("/api/listings")
async def list_listings(limit: int = 100):
    """List marketplace listings"""
    listings = db.get_listings(limit=limit)
    return [l.model_dump() for l in listings]


@app.get("/api/runs")
async def list_runs(limit: int = 100):
    """List pipeline runs"""
    runs = db.get_pipeline_runs(limit=limit)
    return [r.model_dump() for r in runs]


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "0.1.0"}
