from typing import List


# recursion solution
# preorder: root, left, right
# postorder: left, right, root
# solution 1, time complexity O(n^2)
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def build(i, j, n):
            if n <= 0:
                return None
            root = TreeNode(pre[i])
            if n == 1:
                return root
            k = j
            while post[k] != pre[i + 1]:
                k += 1
            l = k - j + 1
            root.left = build(i + 1, j, l)
            root.right = build(i + l + 1, k + 1, n - l - 1)
            return root

        return build(0, 0, len(pre))


# Solution2: we use hash map to decrease time complexity O(n)
def constructFromPrePost(self, pre:List[int], post: List[int]) -> TreeNode:
    def build(i, j, n):
        if n <= 0:
            return None
        root = TreeNode(pre[i])
        if n == 1:
            return root
        k = index[pre[i + 1]]
        l = k - j + 1
        root.left = build(i + 1, j, l)
        root.right = build(i + l + 1, k + 1, n - l - 1)
        return root
    index = {}
    for i in range(len(pre)):
        index[post[i]] = i
    return build(0, 0, len(pre))