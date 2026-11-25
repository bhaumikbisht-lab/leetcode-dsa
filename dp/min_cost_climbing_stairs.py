# 746. Min Cost Climbing Stairs (Easy) — Day 7, 2026-11-25
# Idea: cost to reach a step = its own cost + min(cost of previous two steps).
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for c in cost:
            a, b = b, min(a, b) + c
        return min(a, b)
# Time: O(n) | Space: O(1)
