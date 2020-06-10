def isIsomorphic(s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo","bar"))
print(isIsomorphic("paper","title"))
print(isIsomorphic("aba","baa"))