# 1089 Duplicate Zeros
# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the
# remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.
# Example 1:
#
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
#
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
from typing import List


def duplicateZeros(arr):
    zeros = arr.count(0)
    # initiate how many zeros we want to duplicate
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if i + zeros < n:
            arr[i + zeros] = arr[i]
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0
    return arr


print(duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7]))





















