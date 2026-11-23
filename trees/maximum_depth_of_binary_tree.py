# 104. Maximum Depth of Binary Tree (Easy) — Day 5, 2026-11-23
# Idea: depth of a node = 1 + the deeper of its two subtrees.
from typing import Optional


# Definition for a binary tree node (provided by LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# Time: O(n) | Space: O(h) recursion stack
