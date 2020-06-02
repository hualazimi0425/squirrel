from typing import List


def reverseString(s: List[str]):
    return s[::-1]


def reverseString1(s: List[str]):
    n = len(s)
    i = 0
    j = n - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        # swap
        i += 1
        j -= 1
    return s


print(reverseString(["h", "e", "l", "l", "o"]))
print(reverseString(["H", "a", "n", "n", "a", "h"]))
