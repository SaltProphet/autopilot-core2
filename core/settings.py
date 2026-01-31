"""Settings management for pi-core"""

import os
from typing import Any, Dict

DEFAULTS = {
    "mode": "APPROVAL",
    "max_cost_cents_per_run": 0,
    "banned_categories_json": "[]",
    "hn_query": "",
    "hn_limit": 25,
    "hn_tags": "story",
    "hn_by_date": "true",
}


def load_settings() -> Dict[str, Any]:
    """Load settings from environment variables or defaults"""
    settings = {}
    
    for key, default_value in DEFAULTS.items():
        env_key = f"PI_CORE_{key.upper()}"
        value = os.getenv(env_key, default_value)
        
        # Parse integers
        if key in ("max_cost_cents_per_run", "hn_limit"):
            try:
                settings[key] = int(value)
            except (ValueError, TypeError):
                settings[key] = int(default_value)
        else:
            # Everything else is a string
            settings[key] = str(value)
    
    return settings


def get(key: str, default: Any = None) -> Any:
    """Get a setting value"""
    settings = load_settings()
    return settings.get(key, default)


def update(updates: Dict[str, Any]) -> None:
    """Update settings (persists to environment variables for current process)"""
    for key, value in updates.items():
        if key in DEFAULTS:
            os.environ[f"PI_CORE_{key.upper()}"] = str(value)
