# 70. Climbing Stairs (Easy) — Day 7, 2026-11-25
# Idea: ways(n) = ways(n-1) + ways(n-2) — Fibonacci, keep only two variables.
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
# Time: O(n) | Space: O(1)
