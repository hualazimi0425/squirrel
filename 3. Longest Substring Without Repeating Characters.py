# solution 1: hash map
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    lookup = set()
    longest = 0
    for i in range(n):
        for j in range(i, n):
            if s[j] in lookup:
                break
            else:
                lookup.add(s[j])
        longest = max(longest, len(lookup))
        lookup.clear()
    return longest


# solution 2: sliding window
def lengthOfLongestSubstring2(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    result = 0
    new_dict = {}
    start = 0
    for i in range(n):
        new_dict[ord(s[i])] = new_dict.get(ord(s[i]), 0) + 1
        while new_dict[ord(s[i])] > 1:
            new_dict[ord(s[start])] -= 1
            start += 1
        result = max(result, i - start + 1)
    return result


#print(lengthOfLongestSubstring2("abcabcbb"))
#print(lengthOfLongestSubstring2("bbbb"))
print(lengthOfLongestSubstring2("pwwkew"))
