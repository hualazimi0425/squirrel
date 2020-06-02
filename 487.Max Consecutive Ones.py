def findMaxConsecutiveOnes(nums):
    pre, curr, maxlen = -1, 0, 0
    for num in nums:
        if num == 0:
            pre, curr = curr, 0
        else:
            curr += 1
        maxlen = max(maxlen, pre + curr + 1)
    return maxlen


print(findMaxConsecutiveOnes([1,0,1,1,0]))

