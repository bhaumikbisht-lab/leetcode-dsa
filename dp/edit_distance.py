# 72. Edit Distance (Medium) — Day 9, 2026-11-27
# Idea: if chars match, no cost; else 1 + min(insert, delete, replace) — classic 2D DP, two rows only.
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))
        for i in range(1, m + 1):
            cur = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
            prev = cur
        return prev[n]
# Time: O(m x n) | Space: O(n)
