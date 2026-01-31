from __future__ import annotations

import time
import requests
from typing import Dict, List, Optional

ALGOLIA_SEARCH = "https://hn.algolia.com/api/v1/search"
ALGOLIA_SEARCH_BY_DATE = "https://hn.algolia.com/api/v1/search_by_date"

def search(query: str, limit: int = 25, by_date: bool = True, tags: Optional[str] = "story") -> List[Dict[str, str]]:
    endpoint = ALGOLIA_SEARCH_BY_DATE if by_date else ALGOLIA_SEARCH
    params = {
        "query": query,
        "hitsPerPage": max(1, min(int(limit), 100)),
    }
    if tags:
        params["tags"] = tags

    r = requests.get(endpoint, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()

    out: List[Dict[str, str]] = []
    for h in data.get("hits", []):
        object_id = str(h.get("objectID", ""))
        title = str(h.get("title") or h.get("story_title") or "")
        body = str(h.get("comment_text") or "")
        url = str(h.get("url") or h.get("story_url") or "")
        if not url and object_id:
            url = f"https://news.ycombinator.com/item?id={object_id}"

        out.append(
            {
                "source": "hackernews",
                "source_ref": object_id,
                "title": title,
                "body": body,
                "url": url,
            }
        )

    time.sleep(0.10)
    return out
