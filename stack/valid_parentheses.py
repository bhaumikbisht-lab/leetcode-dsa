# 20. Valid Parentheses (Easy) - https://leetcode.com/problems/valid-parentheses/
# Idea: push opening brackets on a stack, match every closing bracket with the top. Time O(n), Space O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
