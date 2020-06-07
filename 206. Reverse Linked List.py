# solution 1 iteration
class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    curr = head
    nextTemp = ListNode()
    while curr:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    return prev


# solution 2 recursion
def reverseList(head):
    return dfs(head, None)


def dfs(curr, prev):
    if not curr:
        return prev
    next = curr.next
    curr.next = prev
    return dfs(next, curr)
