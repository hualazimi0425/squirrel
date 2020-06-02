# native solution, shouldn't be used in interview
def addBinary(a: str, b: str) -> str:
    return '{0:b}'.format(int(a, 2), int(b, 2))

# solution 2: time complexity O(max(N, M)), where N and M
# are lengths of the input strings a and b


def addBinary1(a: str, b: str) -> str:
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    # fill in zeros to have the same length(long)
    carry = 0
    result = []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        if carry % 2 == 0:
            result.append('0')
        else:
            result.append('1')
        carry //= 2
    if carry == 1:
        result.append('1')
    return ''.join(result[::-1])


print(addBinary1('1010', '1011'))

# solution 3, utilize binary operation instead of addition


def addBinary3(a, b):
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]
