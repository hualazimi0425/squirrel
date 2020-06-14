from typing import List


# solution 1: compare with nums[0]
def findMin(nums: List[int]) -> int:
    n = len(nums)
    l, r = 0, n - 1
    if nums[0] < nums[n - 1]:
        return nums[0]
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= nums[0]:
            l = mid + 1
        else:
            r = mid
    return nums[l]


# solution 2: compare with nums[r]
def findMin1(nums: List[int]) -> int:
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]


print(findMin([3, 4, 5, 1, 2]))
