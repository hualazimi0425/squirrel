def reverse(x: int) -> int:
    res = 0
    neg = False
    if x < 0:
        neg = True
        x = -x
    while x > 0:
        mod = x % 10
        x //= 10
        res = res * 10 + mod
    if neg:
        res = -res
    return res if (-2 ** 31 < res < 2 ** 31 - 1) else 0


print(reverse(123))
print(reverse(-123))
print(reverse(120))
