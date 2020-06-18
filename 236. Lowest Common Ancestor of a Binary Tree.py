# solution 1: recursion
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p:'TreeNode', q:'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l if l else r
# solution 2 iteration
    def pathToX(self, root, x):
        if not root:
            return None
        if root.val == x:
            stack = []
            stack.append(x)
            return stack
        leftPath = self.pathToX(root.left, x)
        if leftPath:
            leftPath.append(root.val)
            return leftPath
        rightPath = self.pathToX(root.right, x)
        if rightPath:
            rightPath.append(root.val)
            return rightPath
        return None


    def lowestCommonAncestor2(self, root, p, q):
        return None

