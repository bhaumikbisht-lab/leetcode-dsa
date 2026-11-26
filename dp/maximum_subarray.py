# 53. Maximum Subarray (Medium) — Day 8, 2026-11-26
# Idea: Kadane — at each element, either extend the running sum or start fresh from it.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
# Time: O(n) | Space: O(1)
