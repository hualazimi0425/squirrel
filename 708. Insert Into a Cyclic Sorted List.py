class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# solution 1
class Solution:
    def insert(self, head: 'Node', insertVal: int):
        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return head
        prev, curr = head, head.next
        toInsert = False
        while True:
            if prev.val <= insertVal <= curr.val:
                toInsert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            prev, curr = curr, curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head
# solution 2
# find max of the linked list, insert the node after the max
# if the node.val is larger than max.val or less than min.val
# if the node.val is between max.val and min.val, just find the
# right place to insert it.
class Solution:
    def insert2(self, head, insertVal):
        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return head
        # find max of the linked list
        max_node = head
        while max_node.next != head and max_node.val <= max_node.next.val:
            max_node = max_node.next
        curr = max_node
        min_node = max_node.next
        if insertVal >= max_node.val or insertVal <= min_node.val:
            newNode = Node(insertVal, min)
            max_node.next = newNode
        else:
            while curr.next.val < insertVal:
                curr = curr.next
            newNode = Node(insertVal,curr.next)
            curr.next = newNode
        return head


