# 213. House Robber II (Medium) — Day 9, 2026-11-27
# Idea: circle breaks the line — try both cases (skip first house, or skip last house) and take the better.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            prev2, prev1 = 0, 0
            for x in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
# Time: O(n) | Space: O(1)
