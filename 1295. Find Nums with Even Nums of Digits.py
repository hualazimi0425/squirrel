from typing import List


def findNumbers(nums: List[int]) -> int:
    count = 0

    def helper(n):
        if n < 10:
            return 1
        else:
            return 1 + helper(n // 10)

    for item in nums:
        if helper(item) % 2 == 0:
            count = count + 1
    return count


if __name__ == "__main__":
    print("before main")
    print(findNumbers([12, 345, 2, 6, 7896]))
    print("after main")
