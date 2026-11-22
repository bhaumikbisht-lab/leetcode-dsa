# 34. Find First and Last Position of Element in Sorted Array (Medium) — Day 4, 2026-11-22
# Idea: two binary searches — one for the left bound, one for the right bound.
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bound(first: bool) -> int:
            lo, hi, ans = 0, len(nums) - 1, -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    ans = mid
                    if first:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans
        return [bound(True), bound(False)]
# Time: O(log n) | Space: O(1)
