# solution, time complexity O(n**2), space complexity O(n**2) for hashmap
from typing import List


def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    count = 0
    m = {}
    for a in A:
        for b in B:
            m[a + b] = m.get(a + b, 0) + 1
    for c in C:
        for d in D:
            count += m.get(-(c + d), 0)
    return count


# K Sum II in general
def fourSumCount2(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    m = {}

    def nSumCount(lists: List[List[int]]) -> int:
        addToHash(lists, 0, 0)
        return countComplements(lists, len(lists) // 2, 0)

    def addToHash(lists: List[List[int]], i: int, sum: int) -> None:
        if i == len(lists) // 2:
            m[sum] = m.get(sum, 0) + 1
        else:
            for a in lists[i]:
                addToHash(lists, i + 1, sum + a)

    def countComplements(lists: List[List[int]], i: int, complement: int) -> int:
        if i == len(lists):
            return m.get(complement, 0)
        count = 0
        for a in lists[i]:
            count += countComplements(lists, i + 1, complement - a)
        return count

    return nSumCount([A, B, C, D])
print(fourSumCount2([1, 2], [-2, -1], [-1, 2], [0, 2]))