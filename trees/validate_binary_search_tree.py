# 98. Validate Binary Search Tree (Medium) — Day 5, 2026-11-23
# Idea: every node must stay strictly inside the (low, high) range passed down from its ancestors.
from typing import Optional


# Definition for a binary tree node (provided by LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode], lo: float, hi: float) -> bool:
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return check(node.left, lo, node.val) and check(node.right, node.val, hi)
        return check(root, float('-inf'), float('inf'))
# Time: O(n) | Space: O(h) recursion stack
