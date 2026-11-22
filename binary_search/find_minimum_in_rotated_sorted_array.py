# 153. Find Minimum in Rotated Sorted Array (Medium) — Day 4, 2026-11-22
# Idea: compare mid with hi to shrink the range towards the minimum.
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
# Time: O(log n) | Space: O(1)
