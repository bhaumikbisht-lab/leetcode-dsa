# 997. Find the Town Judge (Easy) — Day 6, 2026-11-25
# Idea: the judge is trusted by everyone (n-1) and trusts nobody — track a trust score per person.
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1   # trusts someone -> cannot be judge
            score[b] += 1   # trusted by someone
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1
# Time: O(n + trust) | Space: O(n)
