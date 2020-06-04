# solution 1: brute force
# solution 2:
import math
from typing import List


def shortestDistance(words: List[str], word1: str, word2: str) -> int:
    n = len(words)
    i1, i2, min_current_dist = -1, -1, n
    for i in range(n):
        if words[i] == word1:
            i1 = i
        elif words[i] == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            min_current_dist = min(min_current_dist, abs(i1 - i2))
    return min_current_dist


print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))