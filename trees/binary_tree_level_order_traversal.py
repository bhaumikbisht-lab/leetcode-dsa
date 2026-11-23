# 102. Binary Tree Level Order Traversal (Medium) — Day 5, 2026-11-23
# Idea: BFS with a queue; process one whole level at a time using the queue size.
from collections import deque
from typing import List, Optional


# Definition for a binary tree node (provided by LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
# Time: O(n) | Space: O(n)
