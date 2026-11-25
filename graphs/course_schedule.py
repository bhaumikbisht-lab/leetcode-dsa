# 207. Course Schedule (Medium) — Day 6, 2026-11-25
# Idea: Kahn's topological sort — take zero-indegree courses first; if all are taken, no cycle exists.
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        q = deque([c for c in range(numCourses) if indegree[c] == 0])
        taken = 0
        while q:
            c = q.popleft()
            taken += 1
            for nxt in graph[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return taken == numCourses
# Time: O(V + E) | Space: O(V + E)
