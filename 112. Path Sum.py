# recursion
def hasPathSum(root):
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right,sum)
#iteration
def hasPathSum2(root):
    if not root:
        return False
    de = [(root.val, sum - root.val)]
    while de:
        node, curr_sum = de.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            de.append(node.right, curr_sum - node.right.val)
        if node.left:
            de.append(node.left, curr_sum - node.left.val)
    return False
