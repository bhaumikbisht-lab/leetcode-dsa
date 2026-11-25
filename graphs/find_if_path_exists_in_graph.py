# 1971. Find if Path Exists in Graph (Easy) — Day 6, 2026-11-25
# Idea: build an adjacency list and BFS from the source — destination reachable means a path exists.
from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = {source}
        q = deque([source])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei == destination:
                    return True
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return False
# Time: O(V + E) | Space: O(V + E)
