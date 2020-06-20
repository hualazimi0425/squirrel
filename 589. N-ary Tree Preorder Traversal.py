# Definition for a Node.
from typing import List


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output

    def preorder1(self, root: 'Node') -> List[int]:
        def traversePreOrder(root, result):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                traversePreOrder(child, result)

        result = []
        if not root:
            return result
        traversePreOrder(root, result)
        return result