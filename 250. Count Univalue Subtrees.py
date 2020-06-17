# https://www.youtube.com/watch?v=7HgsS8bRvjo
# recursion, time complexity O(n^2)
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_unival(self, root):  # a helper function
        if not root:  # empty counts for a unival subtree
            return True
        if not root.left and root.left.value != root.val:
            return False
        if not root.right and root.right.value != root.val:
            return False
        if self.is_unival(root.left) and self.is_unival(root.right):
            return True
        return False

    # next we need to count # of unival subtree
    def count_univals(self, root):
        if not root:
            return 0
        total_count = self.count_univals(root.left) + self.count_univals(root.right)
        if self.is_unival(root):
            total_count += 1
        return total_count


# recursion2 improve it to time complexity O(n), kind of combine the two functions above
# together in one.
def count_univals2(root: Node):  # wrapper
    total_count, is_unival = helper(root)
    return total_count


def helper(root: Node):
    if not root:
        return (0, True)
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    is_unival = True
    if not is_left_unival or not is_right_unival:
        return False
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    if is_unival:
        return (left_count + right_count + 1, True)
    else:
        return (left_count + right_count, False)


print(count_univals2([5, 1, 5, 5, 5, None, 5]))
