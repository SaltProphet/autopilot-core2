"""GitHub problem source adapter"""

import re
from collections import Counter
from datetime import datetime
from typing import List

from pi_core.adapters import ProblemSourceAdapter
from pi_core.config import config
from pi_core.models import Problem, ProblemIntent, ProblemSource, EvidenceSnippet


class GitHubAdapter(ProblemSourceAdapter):
    """Discover problems from GitHub Issues"""

    def __init__(self):
        self.config = config.github

    def is_configured(self) -> bool:
        """Check if GitHub API token is configured"""
        return self.config.enabled and self.config.token is not None

    async def discover_problems(self, limit: int = 100) -> List[Problem]:
        """Discover problems from GitHub Issues"""
        if not self.is_configured():
            return []

        try:
            from github import Github

            g = Github(self.config.token)

            problems = []
            
            # Search for issues with problem-indicating labels
            search_queries = [
                "label:bug is:open",
                "label:enhancement is:open",
                "label:help-wanted is:open",
                "label:question is:open",
            ]

            for query in search_queries:
                try:
                    issues = g.search_issues(
                        query=query,
                        sort="reactions",
                        order="desc",
                    )
                    
                    for issue in issues[:min(25, limit // len(search_queries))]:
                        problem = self._extract_problem(issue)
                        if problem:
                            problems.append(problem)
                            
                except Exception as e:
                    print(f"Error processing query '{query}': {e}")
                    continue

            # Remove duplicates and rank
            seen = set()
            unique_problems = []
            for p in problems:
                if p.title not in seen:
                    seen.add(p.title)
                    unique_problems.append(p)

            unique_problems.sort(
                key=lambda p: (
                    p.confidence_score * 0.4
                    + p.recency_score * 0.3
                    + min(p.frequency_score / 20, 1.0) * 0.3
                ),
                reverse=True,
            )

            return unique_problems[:limit]

        except Exception as e:
            print(f"Error discovering problems from GitHub: {e}")
            return []

    def _extract_problem(self, issue) -> Problem:
        """Extract problem details from a GitHub issue"""
        text = issue.title + " " + (issue.body or "")
        
        # Classify intent
        intent = self._classify_intent(issue, text)
        
        # Extract keywords
        keywords = self._extract_keywords(text)
        
        # Calculate scores
        confidence_score = self._calculate_confidence(issue)
        frequency_score = issue.reactions["total_count"]
        recency_score = self._calculate_recency(issue.created_at)
        
        # Create evidence
        evidence = [
            EvidenceSnippet(
                text=issue.title[:200],
                source_url=issue.html_url,
                author=issue.user.login if issue.user else None,
                timestamp=issue.created_at,
            )
        ]

        return Problem(
            title=issue.title[:100],
            description=(issue.body or issue.title)[:500],
            intent=intent,
            source=ProblemSource.GITHUB,
            confidence_score=confidence_score,
            frequency_score=frequency_score,
            recency_score=recency_score,
            evidence=evidence,
            keywords=keywords,
        )

    def _classify_intent(self, issue, text: str) -> ProblemIntent:
        """Classify the intent of the problem"""
        labels = [label.name.lower() for label in issue.labels]
        text_lower = text.lower()
        
        if "bug" in labels or any(word in text_lower for word in ["bug", "error", "crash"]):
            return ProblemIntent.PAIN
        elif "enhancement" in labels or "feature" in labels:
            return ProblemIntent.REQUEST
        else:
            return ProblemIntent.WORKAROUND

    def _extract_keywords(self, text: str, top_n: int = 10) -> List[str]:
        """Extract keywords from text"""
        words = re.findall(r'\b\w+\b', text.lower())
        
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
            "been", "being", "have", "has", "had", "do", "does", "did", "will",
            "would", "should", "could", "may", "might", "can", "i", "you", "he",
            "she", "it", "we", "they", "this", "that", "these", "those",
        }
        
        words = [w for w in words if w not in stop_words and len(w) > 3]
        counter = Counter(words)
        return [word for word, _ in counter.most_common(top_n)]

    def _calculate_confidence(self, issue) -> float:
        """Calculate confidence score"""
        score = 0.5
        
        # Boost for reactions
        reactions = issue.reactions["total_count"]
        if reactions > 5:
            score += 0.2
        if reactions > 20:
            score += 0.1
        
        # Boost for comments
        if issue.comments > 3:
            score += 0.1
        if issue.comments > 10:
            score += 0.1
        
        return min(score, 1.0)

    def _calculate_recency(self, created_at: datetime) -> float:
        """Calculate recency score"""
        age_days = (datetime.now(created_at.tzinfo) - created_at).days
        
        if age_days <= 7:
            return 1.0
        elif age_days <= 30:
            return 0.7
        elif age_days <= 90:
            return 0.4
        else:
            return 0.2
