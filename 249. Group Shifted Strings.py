# solution
# key question: how to design key in the hashtable
# Strings in the same group has one common thing:
# if each ord of letter substract ord of first letter and mod by 26,
# they should have the same ord of string
# acf: 025  bdg:136 (if substract by 1) ->025
import collections
from typing import List


def groupStrings(strings: List[str]) -> List[List[str]]:
    # design hash fucntion
    def hash_fct(s):
        return tuple((ord(c) - ord(s[0]) % 26 for c in s))
    groupby = collections.defaultdict(list)
    for s in strings:
        groupby[hash_fct(s)].append(s)
    return groupby.values()

print(groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
