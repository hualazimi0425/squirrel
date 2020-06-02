import sys
from typing import List


# solution 1, time complexity O(n^3)

def minSubArrayLen(s: int, nums: List[int]) -> int:
    n = len(nums)
    ans = sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            sum_s = 0
            for k in range(i, j + 1):
                sum_s += nums[k]
                # here can be improved
            if sum_s >= s:
                ans = min(ans, j - i + 1)
                break
    if ans != sys.maxsize:
        return ans
    else:
        return 0


# solution 2 better brute force, time complexity O(n^2), space complexcity
# O(n)
def minSubArrayLen2(s: int, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    ans = sys.maxsize
    sum_s = [0] * n
    sum_s[0] = nums[0]
    for i in range(1, n):
        sum_s[i] = sum_s[i - 1] + nums[i]
        for i in range(n):
            for j in range(i, n):
                sum_a = sum_s[j] - sum_s[i] + nums[i]
                if sum_a >= s:
                    ans = min(ans, (j - i + 1))
                    break
    if ans != sys.maxsize:
        return ans
    else:
        return 0

# solution 3:
# 1. initialize left pointer to 0 and add sum to 0
# 2. iterate over nums:
#    1) add nums[i] to sum
#    2) while sum is greater than or equal to s:
#       1.. update ans = min(ans, i+1-left),
#           where i + 1 - left is size of curr subarray
#       2.. it means that the first index can safely be
#           incremented, since, the minimum subarray starting
#           with this index with sum>= s has been achieved
#       3.. subtract nums[left] from sum and increment left.


def minSubArrayLen3(s: int, nums: List[int]) -> int:
    n = len(nums)
    # sum of nums element to compare with s
    sums = 0
    # left window boundary
    left = 0
    # final return value
    ans = sys.maxsize
    for i in range(n):
        sums += nums[i]
        while sums >= s:
            ans = min(ans, i + 1 - left)
            sums = sums - nums[left]
            left += 1
    if ans != sys.maxsize:
        return ans
    else:
        return 0


print(minSubArrayLen3(7, [2, 3, 1, 2, 4, 3]))
#print(minSubArrayLen3(7, [2, 3, 1, 2, 4, 3]))