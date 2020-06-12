def guess(m):
    pass


def guessNumber(n) -> int:
    l, r = 1, n + 1 
    while l < r:
        m = (l + r) // 2 
        if guess(m) == 0:
            return m
        if guess(m) < 0:
            r = m 
        else: 
            l = m + 1 
    return l 