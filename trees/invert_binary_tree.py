# 226. Invert Binary Tree (Easy) — Day 5, 2026-11-23
# Idea: recursively swap the left and right child of every node.
from typing import Optional


# Definition for a binary tree node (provided by LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
# Time: O(n) | Space: O(h) recursion stack
