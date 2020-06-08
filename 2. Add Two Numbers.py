class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        # initiate dummy head of return list
        # p, q as head of l1, l2
        # carry to be 0
        dummy_head = ListNode(0)
        curr = dummy_head
        p = l1
        q = l2
        carry = 0
        # loop until both p and q ends
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sums = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        if not l2:
            return l1
        return self.helper(l1, l2, 0)

    def helper(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if not l1 and not l2 and not carry:
            return None
        val = 0
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        if carry:
            val += carry
        cur = ListNode(val % 10)
        carry = val // 10
        cur.next = self.helper(l1, l2, carry)
        return cur
