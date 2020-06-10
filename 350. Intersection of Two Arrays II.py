import collections
from typing import List


# solution 1: hash map: time complexity O(n+m), space complexity O(min(n,m))

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        return intersect(nums2, nums1)
    lookup = collections.defaultdict(int)
    for i in nums1:
        lookup[i] += 1
    result = []
    for i in nums2:
        if lookup[i] > 0:
            result.append(i)
            lookup[i] -= 1
    return result
print(intersect([1, 2, 2, 1], [2, 2]))
# solution 2: sort first, time complexity O(nlogn + mlogm)
def intersect2(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    result = []
    i, j= 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
            #k += 1
    return result
print(intersect2([1, 2, 2, 1], [2, 2]))

