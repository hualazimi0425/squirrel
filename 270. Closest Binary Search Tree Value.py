class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self. left = left
def closestValue(root:TreeNode, target: float) -> int:
    node = root
    candidate = node.val
    while node:
        candidate = min((candidate, node.val), key=lambda x: abs(x - target))
        if node.val < target:
            node = node.right
        elif node.val > target:
            node = node.left
        else:
            return node.val
    return candidate 