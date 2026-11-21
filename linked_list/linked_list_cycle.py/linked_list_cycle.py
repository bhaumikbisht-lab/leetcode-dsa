# 141. Linked List Cycle (Easy) — Day 3, 2026-11-21
# Idea: Floyd's tortoise & hare — if the fast pointer ever meets the
# slow pointer, there is a cycle; if fast hits the end, there is none.
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# Time: O(n) | Space: O(1)
