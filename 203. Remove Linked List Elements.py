# Approach : sentinel Node
# Initiate sentinel node as ListNode(0) and set it to be
# the new head: sentinel.next = head
# Initiate two pointers to track the current node and its
# predecessor: curr and prev.
# while curr is not a null pointer.
#   compare the value of the current node with the value to
#   delete.
#       in the values are equal, delete the current node:
#       prev.next = curr.next
#   otherwise, set predecessor to be equal to the current
#   node.
#   Move to the next Node: curr = curr.next
#   Return sentinel.next

class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    sentinel = ListNode(0)
    sentinel.next = head
    prev, curr = sentinel, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return sentinel.next
