# 300. Longest Increasing Subsequence (Medium) — Day 7, 2026-11-25
# Idea: keep tails[i] = smallest possible tail of an increasing subsequence of length i+1; binary-search each number's place.
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
# Time: O(n log n) | Space: O(n)
