# pi-core: AI-Powered Problem Discovery & Product Generation

**Transform problems into products automatically.**

pi-core is an AI-powered system that discovers real problems from Reddit and GitHub, defines viable products, generates complete content and assets, and packages them for marketplace listing.

## 🚀 Quickstart (30 seconds)

Try the demo with one command:

```bash
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python demo.py
```

Or using editable install:

```bash
python -m venv .venv && source .venv/bin/activate && pip install -e . && python demo.py
```

The demo runs without any API credentials and produces:
- ✅ A complete product spec (stored in `data/demo.db`)
- ✅ Generated assets including markdown docs and config files (in `artifacts/`)
- ✅ A marketplace-ready ZIP bundle with pricing

## 🎯 What It Does

**Demo-Ready MVP Features:**

1. **Problem Discovery Engine** - Pulls real problems from Reddit and GitHub Issues
2. **Product Definition Engine** - Converts problems into shippable product specs
3. **Content & Asset Generator** - Creates complete product bundles (code, docs, templates)
4. **Marketplace Packaging** - Generates ready-to-post Gumroad listings
5. **Control Dashboard** - Web UI for monitoring and controlling the pipeline

## 🏁 Getting Started

### Run the Demo (No API Keys Required)

The quickest way to see pi-core in action:

```bash
# Clone and setup
git clone https://github.com/SaltProphet/autopilot-core2.git
cd autopilot-core2

# One-liner to install and run
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python demo.py
```

This creates a complete product pipeline with mock data - no API credentials needed!

### Full Installation

For production use with live data sources:

```bash
# Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Or install in editable mode for development
pip install -e .

# Configure API credentials (optional)
cp .env.example .env
# Edit .env with your Reddit and GitHub API credentials

# Run the dashboard
python main.py
```

Visit http://localhost:8000 to access the control dashboard.

## 🔑 API Configuration (Optional)

## 🔑 API Configuration (Optional)

The demo works without any API credentials. For live problem discovery from Reddit and GitHub:

**Reddit API:**
1. Visit https://www.reddit.com/prefs/apps
2. Create an app and get your client ID and secret
3. Add to `.env`:
```bash
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
```

**GitHub API:**
1. Visit https://github.com/settings/tokens
2. Generate a personal access token
3. Add to `.env`:
```bash
GITHUB_TOKEN=your_github_token_here
```

Secrets are managed via the `.env.example` file - never commit actual credentials!

## 📊 Dashboard Features

### Control Plane

- **Source Toggles**: Enable/disable Reddit and GitHub sources
- **Manual Approval**: Require approval before publishing
- **Kill Switch**: Global stop for all pipeline execution

### Pipeline Visualization

Watch your pipeline progress through stages:
1. **Discover** - Find problems from sources
2. **Define** - Create product specifications
3. **Build** - Generate content and assets
4. **Package** - Create marketplace listings

### Real-Time Monitoring

- View discovered problems with confidence scores
- Browse generated products
- Preview marketplace listings with pricing
- Track pipeline runs with detailed logs

## 🏗️ Architecture

### Core Engines

- **ProblemDiscoveryEngine**: Aggregates problems from multiple sources
- **ProductDefinitionEngine**: Transforms problems into product specs
- **ContentGeneratorEngine**: Generates assets (scripts, guides, templates, tools)
- **MarketplacePackagingEngine**: Creates marketplace-ready bundles

### Extensibility via Adapters

```python
# Problem sources
- RedditAdapter
- GitHubAdapter
- (Add more: StackOverflow, HackerNews...)

# Product builders
- ScriptBuilder
- ToolBuilder
- GuideBuilder
- TemplateBuilder

# Marketplaces
- GumroadAdapter (future)
- (Add more platforms...)
```

### Data Models

- **Problem**: Discovered issue with evidence and scoring
- **Product**: Product definition with features and personas
- **MarketplaceListing**: Ready-to-publish listing with pricing
- **PipelineRun**: Execution tracking with logs and artifacts

## 📁 Project Structure

```
pi-core/
├── pi_core/
│   ├── models/          # Data models (Pydantic + SQLAlchemy)
│   ├── engines/         # Core processing engines
│   ├── adapters/        # Extensible source/marketplace adapters
│   ├── pipeline/        # Orchestration and execution
│   ├── ui/              # FastAPI web dashboard
│   ├── config.py        # Configuration management
│   └── database.py      # Database layer (SQLite)
├── demo.py              # Demo script (no API keys needed)
├── main.py              # Dashboard entry point
├── requirements.txt     # Dependencies
└── pyproject.toml       # Project metadata
```

## 🎮 Usage Examples

### Full Pipeline Run

```python
from pi_core.config import config
from pi_core.database import Database
from pi_core.pipeline import PipelineRunner

# Initialize
config.ensure_directories()
db = Database(config.pipeline.data_dir / "pi_core.db")
runner = PipelineRunner(db)

# Run full pipeline
run = await runner.run_full_pipeline()
print(f"Status: {run.status}")
```

### Restart from Specific Stage

```python
from pi_core.models import PipelineStage

# Restart from Build stage with existing problem
run = await runner.run_full_pipeline(
    problem_id="existing-problem-id",
    start_from=PipelineStage.BUILD
)
```

## 🛡️ Guardrails

Built-in safety mechanisms:

- **Max Products Per Day**: Limit pipeline execution frequency
- **Manual Approval**: Review before publishing
- **Kill Switch**: Emergency stop for all operations
- **Error Surface**: No silent failures - all errors visible in UI

## 📦 Generated Artifacts

Each product generates:

- **Documentation**: README, USAGE, INTEGRATION guides
- **Source Code**: Scripts, tools, or templates
- **Configuration**: Ready-to-use config files
- **Marketplace Assets**: ZIP bundle with all files
- **Listing Details**: Title, description, pricing, FAQ

## 🎯 Demo Definition of Done

### ✅ Must Work

- [x] Pull real problems from at least one source
- [x] Produce a complete product bundle
- [x] Generate a ready-to-post marketplace listing
- [x] Show logs + artifacts in UI

### ❌ Does NOT Include (Yet)

- Multi-tenant authentication
- Scaling infrastructure
- Auto-publishing to marketplaces
- "AI business in a box" claims

## 🔧 Development

### Install Dev Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run Tests

```bash
pytest
```

### Code Quality

```bash
# Format
black pi_core/

# Lint
ruff check pi_core/
```

## 🚦 API Endpoints

- `GET /` - Dashboard UI
- `GET /api/config` - Get configuration
- `POST /api/config/update` - Update configuration
- `POST /api/pipeline/run` - Start pipeline run
- `GET /api/pipeline/status` - Get current status
- `GET /api/problems` - List discovered problems
- `GET /api/products` - List generated products
- `GET /api/listings` - List marketplace listings
- `GET /api/runs` - List pipeline runs
- `GET /health` - Health check

## 📝 License

MIT License - Use freely in your projects.

## 🤝 Contributing

Contributions welcome! This is an MVP focused on demonstrating core functionality.

## 📮 Support

For questions or issues, open a GitHub issue.