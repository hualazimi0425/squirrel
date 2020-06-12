import collections
import heapq
from typing import List
from collections import Counter


# solution 1: min heap: time complexity O(n) + O(nlogk), space complexity O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == len(nums):
        return nums
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


# solution2: bucket sorting， time complexity O(n), space complexity: O(n)
def topKFrequent2(nums: List[int], k: int) -> List[int]:
    counts = collections.Counter(nums)
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num in counts.keys():
        buckets[counts[num]].append(num)
    ans = []
    for i in range(n, 0, -1):
        ans += buckets[i]
        if len(ans) == k:
            return ans
    return ans


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent2([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent2([1, 1, 1, 2, 2, 3, 4, 4], 3))
