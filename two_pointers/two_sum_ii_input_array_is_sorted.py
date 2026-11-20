# 167. Two Sum II - Input Array Is Sorted (Medium) - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Idea: array is sorted, so two pointers move by sum comparison. Time O(n), Space O(1)
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target: return [l + 1, r + 1]
            if total < target: l += 1
            else: r -= 1
