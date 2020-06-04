from typing import List


def shortestWordDistance(words: List[str], word1: str, word2: str) -> int:
    n = len(words)
    min_distance = n
    w1, w2 = -1, -1
    for i in range(n):
        if words[i] == word1:
            if word1 == word2:
                w1 = w2
                w2 = i
            else:
                w1 = i
        if words[i] == word2:
            w2 = i
        if w1 != -1 and w2 != -1:
            min_distance = min(min_distance, abs(w1 - w2))
    return min_distance


print(shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes"))
