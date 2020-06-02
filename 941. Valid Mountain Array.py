def validMountainArray(A):
    n = len(A)
    i = 0
    # walk up
    while i < n - 1 and A[i] < A[i + 1]:
        i += 1
    # peak can't be the first or the last element
    if i == 0 or i == n - 1:
        return False
    # walk down
    while i < n - 1 and A[i] > A[i + 1]:
        i += 1
    return i == n - 1


def validMountainArray2(A):
    i, j, n = 0, len(A) - 1, len(A)
    while i < n - 1 and A[i] < A[i + 1]:
        i += 1
    while j > 0 and A[j - 1] > A[j]:
        j -= 1
    return 0 < i == j < n - 1


print(validMountainArray([0, 2, 3, 4, 5, 2, 1, 0]))
print(validMountainArray([0, 2, 3, 3, 5, 2, 1]))

print('2nd solution' + ' ' + str(validMountainArray2([0, 2, 3, 4, 5, 2, 1, 0])))
print('2nd solution' + ' ' + str(validMountainArray2([0, 2, 3, 3, 5, 2, 1])))

