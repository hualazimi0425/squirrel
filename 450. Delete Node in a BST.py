class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSuccessor(self, root: TreeNode):
        curr = root.right
        while curr and curr.left:
            curr = curr.left
        return curr
    def deleteNode(self, root: TreeNode, key: int):
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            p = self.findSuccessor(root)
            root.val = p.val
            root.right = self.deleteNode(root.right, p.val)
            return root
        return root
