def firstUniqChar(s: str) -> int:
    hash_map = {}
    n = len(s)
    for i in range(n):
        hash_map[s[i]] = hash_map.get(s[i], 0) + 1
    # find the index
    for i in range(n):
        if hash_map[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
