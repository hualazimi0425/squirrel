# solution 1: linear scan
def findPeakElement(nums):
    n = len(nums)
    # deal with base cases
    for x in range(1, n - 1):
        if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
            return x
    # if [1] should return 0, since left is -inf and right is -inf
    # 1 IS peak element
    if nums[0] < nums[n - 1]:
        return n - 1
    else:
        return 0
# solution 2: binary search
# if find ascending trend, get
# rid of the left part, if find
# descending order, get rid of
# the right part
def findPeakElement1(nums):
    if len(nums) == 1:
        return 0
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l)//2
        if nums[m] < nums[m + 1]:
            l = m + 1
        else:
            r = m
    return l
