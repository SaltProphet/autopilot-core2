#!/usr/bin/env python3
"""
Demonstration script for the refactored pi-core system
Shows how the Hacker News-based pipeline works
"""

import sys
sys.path.insert(0, '.')

def main():
    print("=" * 60)
    print("Pi-Core Refactored Demo: Reddit → Hacker News")
    print("=" * 60)
    print()
    
    # 1. Settings Configuration
    print("1. SETTINGS CONFIGURATION")
    print("-" * 60)
    from core import settings
    
    # Configure settings for HN search
    settings.update({
        'mode': 'APPROVAL',
        'hn_query': 'python programming',
        'hn_limit': 10,
        'hn_tags': 'story',
        'hn_by_date': 'true',
        'max_cost_cents_per_run': 100,
    })
    
    s = settings.load_settings()
    print("Current Settings:")
    for key, value in s.items():
        print(f"  {key}: {value} ({type(value).__name__})")
    print()
    
    # 2. Connector Overview
    print("2. HACKER NEWS CONNECTOR")
    print("-" * 60)
    from connectors.hackernews import ALGOLIA_SEARCH_BY_DATE, ALGOLIA_SEARCH
    print(f"Using Algolia HN API (no authentication required)")
    print(f"  - Search endpoint: {ALGOLIA_SEARCH}")
    print(f"  - Search by date: {ALGOLIA_SEARCH_BY_DATE}")
    print()
    print("The connector will:")
    print("  1. Query Hacker News via Algolia API")
    print("  2. Filter by tags (e.g., 'story', 'comment')")
    print("  3. Return structured results with title, body, url")
    print("  4. Include source reference (HN item ID)")
    print()
    
    # 3. Pipeline Validation
    print("3. PIPELINE VALIDATION")
    print("-" * 60)
    from pipelines.run_mvp import run_discovery_pipeline
    
    print("Pipeline features:")
    print("  ✓ Validates hn_query is not empty")
    print("  ✓ Uses settings from core.settings")
    print("  ✓ Stores signals to database (if path provided)")
    print("  ✓ Returns structured problem signals")
    print()
    
    # Test empty query validation
    import os
    os.environ['PI_CORE_HN_QUERY'] = ''
    try:
        run_discovery_pipeline(db_path=None)
        print("  ✗ Empty query validation failed")
    except RuntimeError as e:
        print(f"  ✓ Empty query validation: '{e}'")
    print()
    
    # 4. UI Application
    print("4. UI APPLICATION")
    print("-" * 60)
    from ui.app import app, SettingsPatch
    
    print(f"FastAPI Application: {app.title} v{app.version}")
    print()
    print("Available endpoints:")
    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            methods = ', '.join(route.methods)
            print(f"  {methods:15} {route.path}")
    print()
    
    print("SettingsPatch model fields:")
    for field_name, field_info in SettingsPatch.model_fields.items():
        print(f"  - {field_name}: {field_info.annotation}")
    print()
    
    # 5. Summary
    print("5. REFACTORING SUMMARY")
    print("-" * 60)
    print("Changes completed:")
    print("  ✓ Removed: Reddit connector and settings")
    print("  ✓ Added: Hacker News connector (connectors/hackernews.py)")
    print("  ✓ Created: core/settings.py with HN-specific settings")
    print("  ✓ Created: pipelines/run_mvp.py with HN discovery")
    print("  ✓ Created: ui/app.py with updated SettingsPatch")
    print("  ✓ Updated: .env.example (removed Reddit/GitHub credentials)")
    print()
    print("Key improvements:")
    print("  ✓ No API keys required (public Algolia endpoint)")
    print("  ✓ Settings validation (hn_query required)")
    print("  ✓ Type-safe settings (ints vs strings)")
    print("  ✓ Clean separation of concerns")
    print()
    
    # 6. Usage Example
    print("6. USAGE EXAMPLE")
    print("-" * 60)
    print("To use the refactored system:")
    print()
    print("  # 1. Set environment variables (optional)")
    print("  export PI_CORE_HN_QUERY='python'")
    print("  export PI_CORE_HN_LIMIT=25")
    print("  export PI_CORE_DB_PATH='./data/pi_core.db'")
    print()
    print("  # 2. Run the pipeline")
    print("  python pipelines/run_mvp.py")
    print()
    print("  # 3. Start the UI server")
    print("  uvicorn ui.app:app --host 0.0.0.0 --port 8000")
    print()
    print("  # 4. Access the API")
    print("  curl http://localhost:8000/api/settings")
    print()
    
    print("=" * 60)
    print("Demo Complete! System ready for Hacker News integration.")
    print("=" * 60)

if __name__ == '__main__':
    main()
