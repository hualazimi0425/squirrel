class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iteration
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return None
# recursion
    def searchBST1(self, root: TreeNode, val: int):
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
