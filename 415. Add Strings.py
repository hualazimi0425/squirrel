def addStrings(num1: str, num2: str) -> str:
    carry = 0
    a = list(num1)
    b = list(num2)
    res = ''
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        res = str(carry % 10) + res
        carry //= 10
    return res


print(addStrings('123','315'))
