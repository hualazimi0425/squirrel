# solution 1 -- string manipulation
# time complexity O((N-L)*L), we compute a
# substring of length L in the loop, which is
# executed (N-L) times. Space complexity O(1)
# Drawback of this algorithm is that one compares
# absolutely all substrings of Length L with the
# needle. There is no need for that.


def strStr(haystack, needle):
    n = len(haystack)
    l = len(needle)
    if n < l:
        return -1
    for i in range(0, n - l + 1):
        if haystack[i:i + 2] == needle:
            return i
    return -1


# solution 2:
# 1. Move pn till you'll find the first character of the needle string in the haystack
# 2. Compute the max string match by increasing pn, pL and curr_len in the case of
# equal characters.
# 3. If you managed to get the full match, curr_len == L, return the start position
# of that match, pn-L.
# 4. If didn't, backtrack: pn = pn - curr_len + 1, pL = 0, curr_len = 0
# Time complexity: O((N-L)*L) in the worst case, and O(N)

def strStr2(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return 0
    pn = 0
    while pn < n - m + 1:
        # first element didn't match, should have condition
        # pn < n - m + 1 here, otherwise, haystack[pn] will grow
        # to more than n - m + 1 as pn +=1
        while pn < n - m + 1 and haystack[pn] != needle[0]:
            pn += 1
            # compute the max match string
        curr_len, pl = 0, 0
        while pl < m and pn < n and haystack[pn] == needle[pl]:
            pn += 1
            pl += 1
            curr_len += 1
            # if the whole needle string is found,
        # return its start position
        if curr_len == m:
            return pn - m
            # otherwise, backrack
        pn = pn - curr_len + 1
    return -1


print(strStr2("hello", "ll"))
print(strStr2("blackberry", "ll"))
print(strStr2("hello", "blackberry"))
