# solution 1: utilize Array to hold in-order traversal result
# time complexity O(n), space complexity O(n)
# next() would take O(1)
# hasNext() take O(1)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root: TreeNode):
        # array hold in-order traversal result
        self.nodes_sorted = []
        # pointer to next smallest element in BST
        self.index = 1
        # call the flatten the input binary search tree
        self._inorer(root)

    # implement inorder traversal algo.
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self):
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self):
        return self.index < len(self.nodes_sorted) - 1

class BSTIterator2:
    def __init__(self, root: TreeNode):
        self.node = root
        self.stack = []
    def next(self):
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        self.node = self.stack.pop()
        ret_val = self.node.val
        self.node = self.node.right
        return ret_val
    def hasNext(self):
        return self.stack or self.node