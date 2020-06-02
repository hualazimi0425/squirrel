# Notice that the sum of i, j, of number in same diagonal are the same.
import collections


def findDiagonalOrder(matrix):
    result = []
    dd = collections.defaultdict(list)
    # use list as the default factory, it's easy to group a sequence
    # of key-value pairs into a dictionary of lists.
    n = len(matrix)
    m = len(matrix[0])
    for i in range(0, n):
        for j in range(0, m):
            dd[i + j + 1].append(matrix[i][j])
            # because i + j is fixed for all elements in same diagonal
    for k in range(n + m - 1):
        if k % 2 != 0:
            result += dd[k][::-1] # reverse order
        else:
            result += dd[k]
    return result


print(findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
