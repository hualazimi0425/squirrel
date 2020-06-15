def squareRoot(num):
    if num < 2:
        return True
    l, r = 2, num + 1
    while l < r:
        mid = l + (r - l) // 2
        potential_square = mid * mid
        if potential_square == num:
            return mid
        elif potential_square < num:
            l = mid + 1
        else:
            r = mid
    return l - 1
def isPerfectSquare(num):
    potential_square_root = squareRoot(num)
    if potential_square_root * potential_square_root == num:
        return True
    else:
        return False



#print(isPerfectSquare(16))
#print(isPerfectSquare(14))
print(squareRoot(4))