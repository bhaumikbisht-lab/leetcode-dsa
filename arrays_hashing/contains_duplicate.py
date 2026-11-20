# 217. Contains Duplicate (Easy) - https://leetcode.com/problems/contains-duplicate/
# Idea: a set drops repeats, so a size mismatch means a duplicate existed. Time O(n), Space O(n)
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
