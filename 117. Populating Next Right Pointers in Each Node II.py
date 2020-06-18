# solution 2 using Queue, 116. Populating Next Right Pointers in Each Node solution still works
import collections


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

#solution 2, modified Problem 116 solution since it maybe a inperfect treee
