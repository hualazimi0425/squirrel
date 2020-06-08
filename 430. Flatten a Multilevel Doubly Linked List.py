class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# solution 1
class Solution(object):
    def flatten(self, head):
        if not head:
            return head
        # pointer
        p = head
        while p:
            # if p doesn't have child
            if not p.child:
                p = p.next
                continue
            # if p has child
            temp = p.child
            # find the tail of child list
            while temp.next:
                temp = temp.next
            # connect tail with p.next, if it is not null
            temp.next = p.next
            if p.next:
                p.next.prev = temp
            # connect p with p.child
            p.next = p.child
            p.child.prev = p
            # and remove p.child
            p.child = None
        return head


# solution 2
from collections import deque


class Solution(object):
    def flatten(self, head):
        if not head:
            return head
        stack = deque()
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
            else:
                if not cur.next and stack:
                    cur.next = stack.pop()
                    cur.next.prev = cur
            cur = cur.next
        return head
