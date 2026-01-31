"""Problem Discovery Engine"""

from typing import List

from pi_core.adapters import ProblemSourceAdapter
from pi_core.adapters.reddit_adapter import RedditAdapter
from pi_core.adapters.github_adapter import GitHubAdapter
from pi_core.models import Problem


class ProblemDiscoveryEngine:
    """Engine for discovering problems from multiple sources"""

    def __init__(self):
        self.adapters: List[ProblemSourceAdapter] = []
        self._register_adapters()

    def _register_adapters(self):
        """Register available problem source adapters"""
        # Register Reddit adapter
        reddit_adapter = RedditAdapter()
        if reddit_adapter.is_configured():
            self.adapters.append(reddit_adapter)

        # Register GitHub adapter
        github_adapter = GitHubAdapter()
        if github_adapter.is_configured():
            self.adapters.append(github_adapter)

    async def discover(self, limit: int = 100) -> List[Problem]:
        """Discover problems from all configured sources"""
        all_problems = []

        for adapter in self.adapters:
            try:
                problems = await adapter.discover_problems(limit=limit)
                all_problems.extend(problems)
            except Exception as e:
                print(f"Error discovering problems from {adapter.__class__.__name__}: {e}")

        # Deduplicate by title similarity
        unique_problems = self._deduplicate_problems(all_problems)

        # Re-rank combined results
        unique_problems.sort(
            key=lambda p: (
                p.confidence_score * 0.4
                + p.recency_score * 0.3
                + min(p.frequency_score / 15, 1.0) * 0.3
            ),
            reverse=True,
        )

        return unique_problems[:limit]

    def _deduplicate_problems(self, problems: List[Problem]) -> List[Problem]:
        """Remove duplicate problems based on title similarity"""
        unique = []
        seen_titles = set()

        for problem in problems:
            # Simple deduplication by title
            title_lower = problem.title.lower()
            if title_lower not in seen_titles:
                seen_titles.add(title_lower)
                unique.append(problem)

        return unique
