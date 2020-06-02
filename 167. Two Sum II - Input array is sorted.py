# solution 1 brute force, time complexity O(n^2)
def twoSum(numbers, target):
    n = len(numbers)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] == target - numbers[j]:
                result.append([i + 1, j + 1])
    return result


# solution 2, two pointers
def twoSum2(numbers, target):
    # two pointers
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1


print(twoSum2([2, 7, 11, 15], 9))

