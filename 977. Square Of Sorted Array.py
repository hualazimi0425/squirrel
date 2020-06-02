import collections
from typing import List


# solution 1, my solution

def sortedSquares(A: List[int]):
    square_list = []
    for i in range(0, len(A)):
        square_list.append(A[i] * A[i])
        square_list.sort()
    return square_list


# solution 2, leetcode

def sortedSquares2(A: List[int]):
    return sorted(x * x for x in A)


# solution 3A, time complexity O(n), space complexity O(n), deque version
def sortedSquares3(A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)


# solution 3B, time complexity O(n), space complexity O(n), list version
def sortedSquares4(A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        if abs(A[l]) > abs(A[r]):
            answer[r - l] = A[l]*A[l]
            l += 1
        else:
            answer[r - l] = A[r]*A[r]
            r -= 1
    return answer


print(sortedSquares4([-4, 1, 3, 6]))
