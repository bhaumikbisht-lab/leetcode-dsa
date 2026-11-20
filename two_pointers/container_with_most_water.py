# 11. Container With Most Water (Medium) - https://leetcode.com/problems/container-with-most-water/
# Idea: two pointers from both ends; always move the shorter wall inward. Time O(n), Space O(1)
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            best = max(best, w * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
