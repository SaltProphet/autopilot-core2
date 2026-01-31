# Pi-Core Refactored: Hacker News Edition

This is the refactored version of pi-core that uses **Hacker News** as the primary discovery source instead of Reddit.

## 🎯 Key Changes

### Removed
- ❌ Reddit API integration
- ❌ Reddit credentials (client_id, client_secret)
- ❌ GitHub credentials

### Added
- ✅ Hacker News connector via Algolia API
- ✅ No authentication required
- ✅ Simplified settings management
- ✅ Clean REST API for configuration

## 📁 New Structure

```
autopilot-core2/
├── connectors/
│   ├── __init__.py
│   └── hackernews.py          # Algolia HN API connector
├── core/
│   ├── __init__.py
│   └── settings.py            # Settings management (HN-specific)
├── pipelines/
│   ├── __init__.py
│   └── run_mvp.py             # Discovery pipeline with HN
├── ui/
│   ├── __init__.py
│   └── app.py                 # FastAPI application
├── .env.example               # Environment variables template
├── demo_refactor.py           # Demonstration script
└── test_refactor.py           # Comprehensive test suite
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Settings

Set environment variables (optional - defaults will be used):

```bash
export PI_CORE_HN_QUERY="python programming"
export PI_CORE_HN_LIMIT=25
export PI_CORE_HN_TAGS="story"
export PI_CORE_HN_BY_DATE="true"
export PI_CORE_DB_PATH="./data/pi_core.db"
```

Or create a `.env` file from the template:

```bash
cp .env.example .env
# Edit .env with your preferred database path
```

### 3. Run the Pipeline

```bash
# Run discovery pipeline
python pipelines/run_mvp.py

# Or use the module
python -m pipelines.run_mvp
```

### 4. Start the API Server

```bash
# Start FastAPI server
uvicorn ui.app:app --host 0.0.0.0 --port 8000

# Access API documentation
# http://localhost:8000/docs
```

## ⚙️ Configuration

### Settings Reference

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `mode` | string | `"APPROVAL"` | Operation mode |
| `max_cost_cents_per_run` | int | `0` | Maximum cost per pipeline run |
| `banned_categories_json` | string | `"[]"` | JSON array of banned categories |
| `hn_query` | string | `""` | **Required** - Hacker News search query |
| `hn_limit` | int | `25` | Maximum results to fetch (1-100) |
| `hn_tags` | string | `"story"` | Filter by tags (story, comment, etc.) |
| `hn_by_date` | string | `"true"` | Sort by date ("true") or relevance ("false") |

### Environment Variables

All settings can be set via environment variables with the `PI_CORE_` prefix:

```bash
PI_CORE_MODE=APPROVAL
PI_CORE_HN_QUERY="python programming"
PI_CORE_HN_LIMIT=50
PI_CORE_HN_TAGS=story
PI_CORE_HN_BY_DATE=true
PI_CORE_DB_PATH=./data/pi_core.db
```

## 📡 API Endpoints

### GET /
Returns API information

```json
{
  "name": "pi-core API",
  "version": "2.0.0",
  "description": "Hacker News problem discovery pipeline"
}
```

### GET /api/settings
Get current settings

```json
{
  "mode": "APPROVAL",
  "max_cost_cents_per_run": 0,
  "hn_query": "python",
  "hn_limit": 25,
  ...
}
```

### PATCH /api/settings
Update settings (partial updates supported)

```bash
curl -X PATCH http://localhost:8000/api/settings \
  -H "Content-Type: application/json" \
  -d '{"hn_query": "python programming", "hn_limit": 50}'
```

### GET /health
Health check endpoint

```json
{
  "status": "healthy",
  "version": "2.0.0"
}
```

## 🔍 Hacker News Connector

The connector uses the public Algolia HN API:

- **Endpoint**: `https://hn.algolia.com/api/v1/search_by_date`
- **No authentication required**
- **Rate limit**: ~10 requests/second (100ms delay between calls)

### Search Parameters

```python
from connectors.hackernews import search

# Search for stories about Python
results = search(
    query="python programming",
    limit=25,
    by_date=True,      # Sort by date (most recent first)
    tags="story"       # Filter to stories only
)
```

### Response Format

Each result contains:

```python
{
    "source": "hackernews",
    "source_ref": "12345",                    # HN item ID
    "title": "New Python Release",
    "body": "Comment text or story text",
    "url": "https://example.com"             # Story URL or HN link
}
```

## 🧪 Testing

### Run Demonstration

```bash
python demo_refactor.py
```

### Run Validation Tests

```bash
python test_refactor.py
```

Expected output:
```
Tests passed: 7/7

🎉 ALL TESTS PASSED! 🎉

The refactored system is ready for use:
  ✓ Uses Hacker News (via Algolia API)
  ✓ No API keys required
  ✓ Settings validated
  ✓ Clean API interface
  ✓ No Reddit dependencies
```

## 📋 Usage Examples

### Example 1: Search for Python Stories

```python
import os
os.environ['PI_CORE_HN_QUERY'] = 'python'
os.environ['PI_CORE_HN_LIMIT'] = '10'

from pipelines.run_mvp import run_discovery_pipeline

signals = run_discovery_pipeline(db_path='./data/test.db')
print(f"Found {len(signals)} signals")
```

### Example 2: Update Settings via API

```python
import requests

# Update query
response = requests.patch(
    'http://localhost:8000/api/settings',
    json={'hn_query': 'javascript frameworks', 'hn_limit': 50}
)

print(response.json())
# {'status': 'success', 'updated': ['hn_query', 'hn_limit'], ...}
```

### Example 3: Fetch Latest HN Stories

```python
from connectors.hackernews import search

# Get latest AI/ML stories
stories = search(
    query='machine learning',
    limit=10,
    by_date=True,
    tags='story'
)

for story in stories:
    print(f"{story['title']}")
    print(f"  URL: {story['url']}")
```

## 🛡️ Validation

### Required Settings

- `hn_query` must not be empty
- `hn_limit` must be between 1 and 100
- Settings are type-validated (ints vs strings)

### Error Handling

```python
from pipelines.run_mvp import run_discovery_pipeline
import os

# Empty query raises error
os.environ['PI_CORE_HN_QUERY'] = ''
try:
    run_discovery_pipeline()
except RuntimeError as e:
    print(e)  # "runtime setting hn_query is empty"
```

## 🔧 Development

### Running Tests

```bash
# Run comprehensive validation
python test_refactor.py

# Test individual components
python -c "from connectors.hackernews import search; print('✓ Connector OK')"
python -c "from core.settings import load_settings; print('✓ Settings OK')"
python -c "from ui.app import app; print('✓ UI OK')"
```

### Code Quality

```bash
# Format code
black connectors/ core/ pipelines/ ui/

# Lint code
ruff check connectors/ core/ pipelines/ ui/

# Type check
mypy connectors/ core/ pipelines/ ui/
```

## 📝 Migration Notes

### From Old pi-core

If migrating from the old Reddit-based pi-core:

1. **Remove Reddit credentials** from environment variables
2. **Set HN query**: `export PI_CORE_HN_QUERY="your search"`
3. **Update imports**: Use new module structure
4. **Update database**: New schema stores HN item IDs

### Key Differences

| Old (Reddit) | New (Hacker News) |
|--------------|-------------------|
| `REDDIT_CLIENT_ID` | Not needed |
| `REDDIT_CLIENT_SECRET` | Not needed |
| `reddit_search()` | `hn_search()` |
| Reddit subreddits | HN query strings |
| Reddit posts | HN stories/comments |

## 🎉 Benefits

- ✅ **No API keys required** - Uses public Algolia endpoint
- ✅ **Simpler setup** - Just set a query string
- ✅ **Better rate limits** - 10 req/sec without authentication
- ✅ **Cleaner data** - HN stories are higher quality
- ✅ **Type-safe** - Proper int vs string handling
- ✅ **Validated** - Empty queries raise clear errors

## 📚 Resources

- [Hacker News Algolia API](https://hn.algolia.com/api)
- [Algolia HN Search](https://hn.algolia.com/)
- [Hacker News](https://news.ycombinator.com/)

## 🐛 Troubleshooting

### "runtime setting hn_query is empty"

Set the HN query:
```bash
export PI_CORE_HN_QUERY="python"
# or
echo 'PI_CORE_HN_QUERY=python' >> .env
```

### "No module named 'connectors'"

Make sure you're running from the project root:
```bash
cd /path/to/autopilot-core2
python pipelines/run_mvp.py
```

### API Connection Errors

The Algolia API is public and requires no authentication. Connection errors typically indicate:
- Network connectivity issues
- Rate limiting (wait 100ms between requests)
- Invalid query parameters

## 📄 License

MIT License - Use freely in your projects.
