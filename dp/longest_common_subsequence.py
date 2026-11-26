# 1143. Longest Common Subsequence (Medium) — Day 8, 2026-11-26
# Idea: if chars match, 1 + LCS of the rest; else take the better of skipping one char from either string.
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur
        return prev[n]
# Time: O(m x n) | Space: O(n)
