from typing import List


# hashmap time complexity O(n), space complexity O(n)
def subarraySum3(nums: List[int], k: int) -> int:
    count, sums, n = 0, 0, len(nums)
    new_dict = {}
    new_dict[0] = 1
    for i in range(n):
        sums += nums[i]
        if sums - k in new_dict.keys():
            count += new_dict.get(sums - k)
        new_dict[sums] = new_dict.get(sums, 0) + 1
    return count


print(subarraySum3([3, 4, 7, 2, -3, 1, 4, 2], 7))
print(subarraySum3([1, 2, 3], 3))
