from typing import List


def arrayPairSum(nums: List[int]) ->int:
    n = len(nums)
    sum_min = 0
    nums.sort()
    for i in range(n):
        if i % 2 == 0:
            sum_min += nums[i]
    return sum_min


print(arrayPairSum([1, 4, 3, 2]))
