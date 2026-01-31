"""MVP pipeline for problem discovery and processing"""

import os
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List

from core import settings
from connectors.hackernews import search as hn_search


def run_discovery_pipeline(db_path: str = None) -> List[Dict[str, str]]:
    """
    Run the discovery pipeline using Hacker News
    
    Args:
        db_path: Optional path to database for persistence
        
    Returns:
        List of discovered signals/problems
    """
    # Get settings
    query = str(settings.get("hn_query", "")).strip()
    limit = int(settings.get("hn_limit", 25))
    tags = str(settings.get("hn_tags", "story")).strip() or None
    by_date = str(settings.get("hn_by_date", "true")).lower() == "true"
    
    # Validate required settings
    if not query:
        raise RuntimeError("runtime setting hn_query is empty")
    
    # Discover signals from Hacker News
    print(f"Searching Hacker News for: {query}")
    print(f"Limit: {limit}, Tags: {tags}, By Date: {by_date}")
    
    signals = hn_search(query=query, limit=limit, by_date=by_date, tags=tags)
    
    print(f"Found {len(signals)} signals from Hacker News")
    
    # If database path provided, store signals
    if db_path:
        store_signals_to_db(signals, db_path)
    
    return signals


def store_signals_to_db(signals: List[Dict[str, str]], db_path: str) -> None:
    """Store discovered signals to database"""
    try:
        from sqlalchemy import create_engine, Column, String, Text, DateTime, MetaData, Table
        from sqlalchemy.orm import sessionmaker
        
        # Create database connection
        engine = create_engine(f"sqlite:///{db_path}", echo=False)
        metadata = MetaData()
        
        # Define problem_signals table
        problem_signals = Table(
            'problem_signals',
            metadata,
            Column('id', String, primary_key=True),
            Column('source', String),
            Column('source_ref', String),
            Column('title', String),
            Column('body', Text),
            Column('url', String),
            Column('discovered_at', DateTime),
        )
        
        # Create tables if they don't exist
        metadata.create_all(engine)
        
        # Insert signals
        Session = sessionmaker(bind=engine)
        session = Session()
        
        try:
            for signal in signals:
                # Generate unique ID
                signal_id = f"{signal['source']}_{signal['source_ref']}"
                
                # Insert or update
                session.execute(
                    problem_signals.insert().values(
                        id=signal_id,
                        source=signal['source'],
                        source_ref=signal['source_ref'],
                        title=signal['title'],
                        body=signal['body'],
                        url=signal['url'],
                        discovered_at=datetime.now(timezone.utc),
                    )
                )
            
            session.commit()
            print(f"Stored {len(signals)} signals to database")
        except Exception as e:
            session.rollback()
            print(f"Error storing signals: {e}")
        finally:
            session.close()
            
    except ImportError:
        print("SQLAlchemy not available, skipping database storage")


def main():
    """Main entry point for pipeline"""
    # Get database path from environment or use default
    db_path = os.getenv("PI_CORE_DB_PATH", "./data/pi_core.db")
    
    # Ensure data directory exists
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Run discovery pipeline
    signals = run_discovery_pipeline(db_path)
    
    # Print summary
    print("\n=== Discovery Summary ===")
    print(f"Total signals discovered: {len(signals)}")
    for i, signal in enumerate(signals[:5], 1):
        print(f"{i}. {signal['title'][:80]}")
    
    return signals


if __name__ == "__main__":
    main()
