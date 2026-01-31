"""Reddit problem source adapter"""

import re
from collections import Counter
from datetime import datetime, timedelta
from typing import List

from pi_core.adapters import ProblemSourceAdapter
from pi_core.config import config
from pi_core.models import Problem, ProblemIntent, ProblemSource, EvidenceSnippet


class RedditAdapter(ProblemSourceAdapter):
    """Discover problems from Reddit"""

    def __init__(self):
        self.config = config.reddit

    def is_configured(self) -> bool:
        """Check if Reddit API credentials are configured"""
        return (
            self.config.enabled
            and self.config.client_id is not None
            and self.config.client_secret is not None
        )

    async def discover_problems(self, limit: int = 100) -> List[Problem]:
        """Discover problems from Reddit"""
        if not self.is_configured():
            return []

        try:
            import praw

            reddit = praw.Reddit(
                client_id=self.config.client_id,
                client_secret=self.config.client_secret,
                user_agent=self.config.user_agent,
            )

            problems = []
            
            # Target subreddits related to development pain points
            subreddits = [
                "programming",
                "learnprogramming",
                "webdev",
                "Python",
                "javascript",
            ]

            for subreddit_name in subreddits:
                try:
                    subreddit = reddit.subreddit(subreddit_name)
                    
                    # Search for posts with problem-indicating keywords
                    for post in subreddit.hot(limit=min(20, limit // len(subreddits))):
                        if self._is_problem_post(post):
                            problem = self._extract_problem(post)
                            if problem:
                                problems.append(problem)
                                
                except Exception as e:
                    print(f"Error processing subreddit {subreddit_name}: {e}")
                    continue

            # Rank by combined score
            problems.sort(
                key=lambda p: (
                    p.confidence_score * 0.4
                    + p.recency_score * 0.3
                    + min(p.frequency_score / 10, 1.0) * 0.3
                ),
                reverse=True,
            )

            return problems[:limit]

        except Exception as e:
            print(f"Error discovering problems from Reddit: {e}")
            return []

    def _is_problem_post(self, post) -> bool:
        """Determine if a post indicates a problem"""
        problem_keywords = [
            "how to",
            "how do i",
            "help",
            "problem",
            "issue",
            "stuck",
            "struggling",
            "can't figure out",
            "doesn't work",
            "not working",
            "error",
            "bug",
            "pain",
            "frustrated",
        ]

        text = (post.title + " " + post.selftext).lower()
        return any(keyword in text for keyword in problem_keywords)

    def _extract_problem(self, post) -> Problem:
        """Extract problem details from a post"""
        text = post.title + " " + post.selftext
        
        # Classify intent
        intent = self._classify_intent(text)
        
        # Extract keywords
        keywords = self._extract_keywords(text)
        
        # Calculate scores
        confidence_score = self._calculate_confidence(post, text)
        frequency_score = post.score  # Use Reddit score as frequency indicator
        recency_score = self._calculate_recency(post.created_utc)
        
        # Create evidence
        evidence = [
            EvidenceSnippet(
                text=post.title[:200],
                source_url=f"https://reddit.com{post.permalink}",
                author=str(post.author),
                timestamp=datetime.fromtimestamp(post.created_utc),
            )
        ]

        return Problem(
            title=post.title[:100],
            description=post.selftext[:500] if post.selftext else post.title,
            intent=intent,
            source=ProblemSource.REDDIT,
            confidence_score=confidence_score,
            frequency_score=frequency_score,
            recency_score=recency_score,
            evidence=evidence,
            keywords=keywords,
        )

    def _classify_intent(self, text: str) -> ProblemIntent:
        """Classify the intent of the problem"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["workaround", "hack", "temporary fix"]):
            return ProblemIntent.WORKAROUND
        elif any(word in text_lower for word in ["request", "feature", "would be nice", "wish"]):
            return ProblemIntent.REQUEST
        else:
            return ProblemIntent.PAIN

    def _extract_keywords(self, text: str, top_n: int = 10) -> List[str]:
        """Extract keywords from text"""
        # Simple keyword extraction
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Filter out common words
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
            "been", "being", "have", "has", "had", "do", "does", "did", "will",
            "would", "should", "could", "may", "might", "can", "i", "you", "he",
            "she", "it", "we", "they", "this", "that", "these", "those",
        }
        
        words = [w for w in words if w not in stop_words and len(w) > 3]
        
        # Count frequency
        counter = Counter(words)
        return [word for word, _ in counter.most_common(top_n)]

    def _calculate_confidence(self, post, text: str) -> float:
        """Calculate confidence score"""
        score = 0.5  # Base score
        
        # Boost for upvotes
        if post.score > 10:
            score += 0.2
        if post.score > 50:
            score += 0.1
        
        # Boost for comments (indicates engagement)
        if post.num_comments > 5:
            score += 0.1
        if post.num_comments > 20:
            score += 0.1
        
        return min(score, 1.0)

    def _calculate_recency(self, created_utc: float) -> float:
        """Calculate recency score (1.0 = very recent, 0.0 = old)"""
        post_time = datetime.fromtimestamp(created_utc)
        age_days = (datetime.now() - post_time).days
        
        if age_days <= 1:
            return 1.0
        elif age_days <= 7:
            return 0.8
        elif age_days <= 30:
            return 0.5
        else:
            return 0.2
