# solution 1: utilize hash table, time complexity O(n), space complexity O(n)
def findDisappearedNumbers(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = 1
    result = []
    for i in range(1, len(nums) + 1):
        if num not in hash_table:
            # if key num is not in hash_table
            result.append(num)
    return result


# solution 2
def findDisappearedNumber2(nums):
    for i in range(0, len(nums)):
        new_index = abs(nums[i]) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1
    result = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            return result.append(i)
    return result
