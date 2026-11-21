# 739. Daily Temperatures (Medium) — Day 3, 2026-11-21
# Idea: monotonic decreasing stack of indices; when a warmer day arrives,
# it answers every colder day still waiting on the stack.
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
# Time: O(n) | Space: O(n)
