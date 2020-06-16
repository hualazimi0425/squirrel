# recursion
def maxDepth(self, root):
    if not root:
        return 0
    else:
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
    return max(left_height, right_height) + 1

# iteration
def maxDepth(self, root):
    stack = []
    if not root:
        stack.append((1, root)) # if single root, has depth 1
    depth = 0
    while stack:
        current_depth, root = stack.pop()
        if root:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))
    return depth