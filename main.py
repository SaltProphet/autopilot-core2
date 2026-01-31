#!/usr/bin/env python3
"""
pi-core main entry point

Launches the web UI dashboard for pi-core
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Starting pi-core dashboard...")
    print("📍 Dashboard: http://localhost:8000")
    print("📍 API Docs: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop")
    
    uvicorn.run(
        "pi_core.ui:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
