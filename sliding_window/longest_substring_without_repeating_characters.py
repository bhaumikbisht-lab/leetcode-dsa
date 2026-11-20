# 3. Longest Substring Without Repeating Characters (Medium) - https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Idea: sliding window + last-seen index map; on a repeat, jump left past the last occurrence. Time O(n), Space O(min(n, alphabet))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            best = max(best, right - left + 1)
        return best
