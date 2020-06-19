class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# solution 1: recursion
class Solution:
    def lowestCommonAncestor(self, root:'TreeNode', p:'TreeNode', q:'TreeNode'):
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
# solution 2: iteration
    def lowestCommonAncestor2(self, root:'TreeNode', p:'TreeNode', q:'TreeNode'):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
