import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

print(groupAnagrams(["are", "bat","ear","code","tab","era"]))