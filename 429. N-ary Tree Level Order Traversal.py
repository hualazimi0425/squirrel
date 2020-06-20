import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# recursion
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[Node]]:
        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []
        if root is not None:
            traverse_node(root, 0)
        return result

    # iteration
    def levelOrder1(self, root: 'Node') -> List[List[Node]]:
        if root is None:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result
