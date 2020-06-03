# two pass hash table
# we reduce the look up time from O(n) to O(1) by trading space for speed
# In first iteration, we add each element's value and its index to the table,
# then, in the second iteration we check if each element's complements
# (target-nums[i]) exists in the table. Beware that the complement must not be nums[i]
# itself.
# Time complexity O(n), space complexity O(n)
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    new_dict = {}
    for i in range(n):
        new_dict[nums[i]] = i
    for i in range(n):
        complement = target - nums[i]
        if complement in new_dict.keys() and new_dict[complement] != i:
            return [i, new_dict[complement]]
    return None


def twoSum2(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    new_dict = {}
    for i in range(n):
        complement = target - nums[i]
        if complement in new_dict.keys():
            return [new_dict[complement], i]
        else:
            new_dict[nums[i]] = i
    return None


print(twoSum([2, 7, 11, 15], 9))
print(twoSum2([2, 7, 11, 15], 9))
