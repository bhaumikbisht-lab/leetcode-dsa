# 19. Remove Nth Node From End of List (Medium) — Day 3, 2026-11-21
# Idea: two pointers n+1 apart — when the front pointer hits the end,
# the back pointer sits just before the node to remove.
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
# Time: O(n) | Space: O(1)
