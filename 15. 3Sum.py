# solution 1
# For each element i in array, find - i
# then it's a two sum question
from typing import List


def twoSum2(nums: List[int], target: int) -> None:
    n = len(nums)
    new_dict = {}
    for i in range(n):
        complement = target - nums[i]
        if complement in new_dict.keys():
            return [complement, nums[i]]
        else:
            new_dict[nums[i]] = i
    return None


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    seen = set()
    result = []
    for i in range(n):
        opposite = -nums[i]
        if opposite not in seen:
            seen.add(opposite)
            for item in seen:
                if twoSum2(nums, opposite) is not None:
                    potential_result = sorted([nums[i], twoSum2(nums, opposite)[0], twoSum2(nums, opposite)[1]])
                if potential_result not in result:
                    result.append(potential_result)
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))


# solution 2
# after sorting the array, we process each value from left to right.
# for value v, we need to find all pairs whose sum is equal to -v. To
# do that, we sue the Two Sum II: Two pointers approach for the rest
# of the array
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    n = len(nums)
    # sort the list in ascending order
    for i in range(n):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i - 1]:
            twoSumII(nums, i, res)


def twoSumII(nums: List[int], i: int, res: List[List[int]]):
    left, right = i + 1, len(nums) - 1
    while left < right:
        sums = nums[i] + nums[left] + nums[right]
        if sums < 0 or (left > i and nums[left] == nums[left - 1]):
            left += 1
        elif sums > 0 or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
            right -= 1
        else:
            res.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
