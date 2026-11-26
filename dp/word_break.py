# 139. Word Break (Medium) — Day 8, 2026-11-26
# Idea: dp[i] = can the prefix of length i be split into dictionary words? Check every split point.
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
# Time: O(n^2) | Space: O(n)
