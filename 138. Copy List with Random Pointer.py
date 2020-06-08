class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        hash_map = {}
        curr = head
        while curr:
            # add curr into hashmap, key is curr, value is newNode with same
            # value as curr
            hash_map[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            # update next pointer
            hash_map.get(curr).next = hash_map.get(curr.next)
            # update random pointer
            hash_map.get(curr).random = hash_map.get(curr.random)
            curr = curr.next
        return hash_map[head]
