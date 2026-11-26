# 62. Unique Paths (Medium) — Day 8, 2026-11-26
# Idea: paths to a cell = paths from above + paths from left; one row is enough.
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
# Time: O(m x n) | Space: O(n)
