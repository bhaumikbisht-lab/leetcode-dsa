# 91. Decode Ways (Medium) — Day 9, 2026-11-27
# Idea: ways(i) = ways(i-1) if s[i] is a valid single digit + ways(i-2) if s[i-1:i+1] is 10..26.
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev2, prev1 = 1, 1 if s[0] != '0' else 0
        for i in range(1, n):
            cur = 0
            if s[i] != '0':
                cur += prev1
            if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                cur += prev2
            prev2, prev1 = prev1, cur
        return prev1
# Time: O(n) | Space: O(1)
