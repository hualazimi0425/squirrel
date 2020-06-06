# solution 1, hash table
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# time complexity O(n)
# space complexity O(n)

def hasCycle(head) -> bool:
    nodeseen = set()
    while head != None:
        if head in nodeseen:
            return True
        else:
            nodeseen.add(head)
        head = head.next
    return False


# solution 2
# time complexity O(n)
# space complexity O(1)
def hasCycle(head) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        # fast move 2 steps
        slow = slow.next
        if fast == slow:
            return True
    return False
