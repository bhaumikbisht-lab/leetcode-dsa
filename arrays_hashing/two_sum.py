# 1. Two Sum (Easy) - https://leetcode.com/problems/two-sum/
# Idea: hashmap of value -> index, look for target - x. Time O(n), Space O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
