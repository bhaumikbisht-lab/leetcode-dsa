# 2. Add Two Numbers (Medium) — Day 3, 2026-11-21
# Idea: walk both lists together like column addition, carrying the tens
# digit forward; a dummy head keeps the result list clean.
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
# Time: O(max(m, n)) | Space: O(max(m, n))
