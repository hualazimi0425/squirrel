# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.
# Example 1:
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


def replaceElements(arr):
    n = len(arr)
    current_max = -1
    for i in range(n - 1, -1, -1):
        current_value = arr[i]  # keep the original value
        arr[i] = current_max  # switch with the original value with current_max value
        current_max = max(current_value, current_max)  # keep updating current_max value with original value
    return arr


print(replaceElements([17, 18, 5, 4, 6, 1]))
