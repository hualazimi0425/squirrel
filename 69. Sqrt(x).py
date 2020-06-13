# solution binary search: time complexity O(logN), space complexity O(1)
def mySqrt(x: int) -> int:
    if x < 2:
        return x
    left, right = 2, x/2
    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot
        if num == x:
            return pivot
        elif num < x:
            left = pivot + 1
        else:
            right = pivot - 1
    return right

# huahua template
def mySqrt1(x: int) -> int:
    l, r = 2, x + 1  # search range [2, x)
    while l < r:
        pivot = l + (r - l) // 2
        square = pivot * pivot
        if square == x:
            return square
        elif square > x:
            r = pivot
        else:
            l = pivot + 1
    return l - 1
print(mySqrt1(8))