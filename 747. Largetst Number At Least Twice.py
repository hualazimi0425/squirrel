def dominantIndex(nums):
    max_index = nums.index(max(nums))
    for i in range(0, len(nums)):
        if nums[i] != nums[max_index] and nums[max_index] < 2 * nums[i]:
            return -1
    return max_index


print(dominantIndex([3, 6, 1, 0]))
print(dominantIndex([1, 2, 3, 4]))
