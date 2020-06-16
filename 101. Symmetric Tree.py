# recursion
def isSymmetric(root):
    return isMirror(root, root)


def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)


# iteration
def isSymmetric2(root):
    q = []  # initiate a queue
    q.append(root)
    q.append(root)
    while q:
        t1 = q.pop(0)
        t2 = q.pop(0)
        if not t1 and not t2:
            continue
        if t1 or t2:
            return False
        if t1.val != t2.val:
            return False
        q.append(t1.left)
        q.append(t2.right)
        q.append(t1.right)
        q.append(t2.left)
    return True
print(isSymmetric2([1,2,2,None,3,None,3]))