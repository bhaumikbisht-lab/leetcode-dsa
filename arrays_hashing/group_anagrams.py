# 49. Group Anagrams (Medium) - https://leetcode.com/problems/group-anagrams/
# Idea: sorted word is the group key in a hashmap. Time O(n * k log k), Space O(n * k)
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())
