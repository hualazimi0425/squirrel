# solution 1 recursion, time complexity O(n), space complexity O(n)
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root:'Node') -> 'Node':
        if not root:
            return None
        if root.next:
            if root.right:
                root.right.next = root.next.left
        if root.left:
            root.left.next = root.right
        self.connect(root.left)
        self.connect(root.right)
        return root
# solution 2: Iteration using Queue, time complexity O(n), space complexity O(n)
def connect(self, root:'Node') ->'Node':
    if not root:
        return root
    # initialize a queue data structure which contains
    # just the root of the tree
    Q = collections.deque([root])
    # outer while loop which iterates over each level
    while Q:
        size = len(Q)
        # iterate over all the nodes on the current level
        for i in range(size):
            # pop a node from the front of the queue
            node = Q.popleft()
            # we don't want to establish any wrong connections. The
            # queue will contain nodes from 2 levels at most at any point in time
            # This check ensures we only don't establish next pointers beyond
            # the end of a level
            if i < size - 1:
                node.next = Q[0]
            # add the children, if any, to the back of the queue
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
    return root


