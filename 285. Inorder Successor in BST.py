class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# if no right child, it's parent can be its' successor
# if it has right child, the leftmost node of right child is
# the successor

class Solution:
    def inorderSuccessor(self, root:'TreeNode', p:'TreeNode') -> 'TreeNode':
        #if has right child, find leftmost of right child
        if p.right:
            return self.findMin(p.right)
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        return succ

    def findMin(self,p):
        while p.left:
            p = p.left
        return p