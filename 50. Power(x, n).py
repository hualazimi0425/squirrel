# solution 1: recursion
def fastpow(x, n):
    if n == 0:
        return 1.0
    half = fastpow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
def myPow(x: float, n: int) -> float:
    n1 = n
    if n1 < 0:
        return 1.0/fastpow(x, n1)
    else:
        return fastpow(x, n)

print(myPow(2.00000, 10))

# solution 2: iteration
def myPow2(x, n) -> float:
    if n < 0:
        return 1.0/myPow(x, -n)
    ans = 1
    current_product = x
    i = n
    while i > 0:
        if i % 2 == 1:
            ans = ans * current_product
        current_product = current_product * current_product
        i = i // 2
    return ans
print(myPow2(2.00000, 10))