class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# time Complexity O(nlogn) because of repeatly visit nodes,space complexity O(n)
# need to visit n nodes to judge if the tree is balanced. O(n)
# then need to visit left subtree, right subtree,  n/2 nodes each to
# judge if left subtree and right subtree are balanced. 2*O(n/2)
class Solution(object):
    def height(self, root):
        if not root:
            return -1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
    def isBalanced(self, root):
        if not root:
            return True
        else:
            return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
# time complexity O(n), visit nodes and record the height
    def isBalancedHelper(self, root):
        if not root:
            return True, -1
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
    def isBalanced(self, root):
        return self.isBalanced(root)[0]

