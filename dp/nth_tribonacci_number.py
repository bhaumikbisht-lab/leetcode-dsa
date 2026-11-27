# 1137. N-th Tribonacci Number (Easy) — Day 9, 2026-11-27
# Idea: T(n) = T(n-1) + T(n-2) + T(n-3) — keep only the previous three numbers.
from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
# Time: O(n) | Space: O(1)
