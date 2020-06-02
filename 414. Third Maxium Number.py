# solution 1: Time complexity O(n), space complexity O(n)
def thirdMax1(nums):
    nums = set(nums)
    maximum = max(nums)
    if len(nums) < 3:
        return maximum
    nums.remove(maximum)
    second_maximum = max(nums)
    nums.remove(second_maximum)
    return max(nums)


# solution 2: kind of implement priority queue with length 3, time complexity O(n), space complexity O(1)
def thirdMax2(nums):
    maximums = set()
    for num in nums:
        maximums.add(num)
        if len(maximums) > 3:
            maximums.remove(min(maximums))
    if len(maximums) < 3:
        return max(maximums)
    else:
        return min(maximums)


print(thirdMax2([2, 2, 3, 1]))
print(thirdMax2([1, 2]))
print(thirdMax2([3, 2, 1]))
