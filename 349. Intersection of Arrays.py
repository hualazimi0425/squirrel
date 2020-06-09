from typing import List


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = set()
    seen = set()
    for num1 in nums1:
        if num1 not in seen:
            seen.add(num1)
    for num2 in nums2:
        if num2 in seen:
            result.add(num2)
    return result