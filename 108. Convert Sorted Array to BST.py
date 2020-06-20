from random import randint
from typing import List

# preorder traversal: node, left, right
# time complexity O(n), space complexity O(n), O(n) to keep the output,
# and O(logn) for the recursion stack
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            # always choose left middle node as a root
            p = (left + right) // 2
            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)

# solution2: preorder traversal, choose right middle node
# as root
    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            # always choose right middle node as a root
            p = (left + right) // 2
            if (left + right) % 2 :
                p += 1
            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)
# solution 3: preorder traversal, choose randome middle node as a root
    def sortedArrayToBST3(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            # always choose left middle node as a root
            p = (left + right) // 2
            if (left + right) % 2 :
                p += randint(0, 1)
            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)