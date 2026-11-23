# 230. Kth Smallest Element in a BST (Medium) — Day 5, 2026-11-23
# Idea: iterative inorder traversal with a stack — inorder of a BST is sorted, so the kth node visited is the answer.
from typing import Optional


# Definition for a binary tree node (provided by LeetCode).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
# Time: O(h + k) | Space: O(h)
