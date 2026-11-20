# 125. Valid Palindrome (Easy) - https://leetcode.com/problems/valid-palindrome/
# Idea: two pointers from both ends, skip non-alphanumeric, compare lowercase. Time O(n), Space O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower(): return False
            l += 1; r -= 1
        return True
