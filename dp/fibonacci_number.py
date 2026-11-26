# 509. Fibonacci Number (Easy) — Day 8, 2026-11-26
# Idea: same as Climbing Stairs — keep only the previous two numbers.
from typing import List


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
# Time: O(n) | Space: O(1)
