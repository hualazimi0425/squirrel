def numJewelsInStones(J:str, S:str) -> int:
    m = len(S)
    lookup = set(J)
    count = 0
    for j in range(m):
        if S[j] in lookup:
            count += 1
    return count

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))