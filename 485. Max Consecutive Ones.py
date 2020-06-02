# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#    The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
from typing import List


# solution 1
def findMaxConsecutiveOnes(nums: List[int]):
    count = 1
    maxcount = 0
    for item in nums:
        if item == 1:
            count = count + 1
        else:
            maxcount = max(count, maxcount)
            # update max each time based on count current value
            count = 0
            # reset count value
    return max(maxcount, count)
    # if last iteration has max ones, it will skip else part, so we need max again, i.e.[1,1,0,1,1,1,1,1]


# solution 2
def findMaxConsecutiveOnes2(nums: List[int]):
    return max(map(len, ''.join(map(str, nums)).split('0')))


# nums = [1,1,0,1,1,1]
# map(str, nums): ['1', '1', '0', '1', '1', '1']
# ''.join(map(str,nums)).split('0'): ['11', '111']
# len is a function

print(findMaxConsecutiveOnes2([1, 1, 1, 0, 0, 1, 1, 1, 1, 1]))
