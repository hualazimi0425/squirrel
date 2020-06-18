import collections


class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# serialization
class Codec:
    def serialize(self,root):
        def rserialize(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) +','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        return rserialize(root, '')

# serialization
    def serialize(self, root):
        def dfs(root):
            if not root:
                res.append("None")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root)
        return ','.join(res)
    def deserialize(self, data):
        def dfs(text) -> TreeNode:
            val = text.popleft()
            if val == 'None':
                return None
            root = TreeNode(val)
            root.left = dfs(text)
            root.right = dfs(text)
            return root
        text = collections.deque(data.split(','))
        return dfs(next)
