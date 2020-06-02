def pivotIndex(nums):
    n = len(nums)
    left_sum, right_sum = 0, 0
    sums = sum(nums)
    for i in range(0, n):
        left_sum = sum(nums[: i])
        right_sum = sums - left_sum - nums[i]
        if left_sum == right_sum:
            return i
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))

