# 198. House Robber (Medium) — Day 7, 2026-11-25
# Idea: at each house, rob it (prev2 + money) or skip it (prev1) — keep the better.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1
# Time: O(n) | Space: O(1)
