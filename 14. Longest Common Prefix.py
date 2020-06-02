# solution 1
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]


# solution 2 Horizontal scanning
# Iterates through the strings[S1, ...Sn], finding
# at each iteration i the longest common prefix of
# string LCP(S1, ...Si) when LCP(S1, ...Si) is an
# empty string, the algorithm ends. Otherwise after
# n iterations, the algorithm returns LCP(S1...Sn)
# Time complexity O(S) where S is the sum of all chars
# in all strings. In the worst case all n strings are the
# same. Space complexity O(1)


def longestCommonPrefix2(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].index != 0:
            prefix = prefix[0, len(prefix) - 1]
            if not prefix:
                return ""
    return prefix


# solution 3 vertical scanning
def longestCommonPrefix3(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0: i]
    return strs[0]
    #set str[0] as base


print(longestCommonPrefix3(['flower', 'flow', 'flight']))
print(longestCommonPrefix3(['cathy', 'baathyis', 'athy']))
print(longestCommonPrefix3(['banana', 'bano', 'banary']))
