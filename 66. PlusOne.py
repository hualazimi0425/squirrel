# solution 1
def PlusOne(digits):
    digits_plus_one = int(''.join(map(str, digits))) + 1
    return list(map(int, str(digits_plus_one)))


def PlusOne2(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


# solution 2
print(PlusOne([1, 2, 3]))
print(PlusOne2([1, 2, 3]))
print(PlusOne2([9, 9, 9]))
print(PlusOne2([1, 9, 9]))

