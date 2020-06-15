# follow up question of 153. Find minimum in rotated
# sorted array
# can't simply use nums[0] > nums[n-1] to decide if
# the array is rotated or not.
# e.g. [2, 2, 2, 2, 3, 2, 2, 2] vs
# [2, 2, 2, 2, 2, 2]
# we need to recursively seek minimum element.
# [2, 2, 2, 2, 3, 2, 2, 2] --> [2, 2, 2, 2] vs [3, 2, 2, 2]
# [2,2] vs [2, 2] --- [3, 2] vs [2, 2]
# till deducted to find min of one or two elements
# time complexity O(n) -> O(n/2) * 2 (2 sub problem in each step)
# so O(n)
from typing import List


def findMin(nums: List[int]):
    return findMinimum(nums, 0, len(nums) - 1)


def findMinimum(nums, l, r):
    if l + 1 >= r:  # if there is only one or two elements, just find min of them
        return min(nums[l], nums[r])
    if nums[l] < nums[r]:  # if sorted array, just return the first element
        return nums[l] < nums[r]
    m = l + (r - l) // 2
    return min(findMinimum(nums, l, m - 1), findMinimum(nums, m, r))
