from typing import List
def split(nums, largestSum):
    pieces = 1
    tmpSum = 0
    for num in nums:
        if tmpSum + num > largestSum:
            # exceed largestSum, need one more pieces
            tmpSum = num
            pieces += 1
        else:
            tmpSum += num
    return pieces

def splitArray(nums: List[int], m: int) -> int:
    l, r = max(nums), sum(nums)
    # l: each element is a subarray, so lower bound is max(nums)
    # r: whole array is a "subarray", so upper bound is sum(nums)
    while l < r:
        mid = l + (r - l) // 2
        pieces = split(nums, mid)
        if pieces > m:
            # m is smaller, so left need
            # need forward
            l = mid + 1
        else:
            r = mid
    return l

print(splitArray([7,2,5,10,8], 2))