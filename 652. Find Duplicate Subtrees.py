import collections


def findDuplicateSubtrees(root):
    count = collections.Counter()
    ans = []
    def collect(node):
        if not node:
            return '#'
        serial = '{},{},{}'.format(node.val, collect(node.left), collect(node.right))
        count[serial] += 1
        if count[serial] == 2:
            ans.append(node)
        return serial
    collect(root)
    return ans