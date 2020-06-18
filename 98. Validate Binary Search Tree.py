# solution 1 recursion
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBSTHelper(T: TreeNode, min_val: float, max_val: float) -> bool:
            if not T:
                return True
            elif T.val <= min_val or T.val >= max_val:
                return False
            else:
                return isBSTHelper(T.left, min_val, T.val) and isBSTHelper(T.right, T.val, max_val)
        return isBSTHelper(root, float('-inf'), float('inf'))

#solution 2 iteration
    def isValidBST2(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf')),]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

