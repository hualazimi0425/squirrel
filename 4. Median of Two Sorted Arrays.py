import sys


def findMedianSortedArray(nums1, nums2):
    a, b = len(nums1), len(nums2)
    if a > b:
        return findMedianSortedArray(nums2, nums1)
    if a == 0:
        return (nums2[(b - 1)//2] + nums2[b//2])//2
    total_len = a + b
    a_start_k, a_end_k = 0, a
    while a_start_k <= a_end_k:
        cut_a = (a_end_k + a_start_k)//2
        cut_b = (total_len + 1)//2 - cut_a
        l1 = nums1[cut_a - 1] if cut_a != 0 else -sys.maxsize
        l2 = nums2[cut_b - 1] if cut_b != 0 else -sys.maxsize
        r1 = nums1[cut_a] if cut_a != a else sys.maxsize
        r2 = nums2[cut_b] if cut_b != b else sys.maxsize
        if l1 > r2:
            a_end_k = cut_a - 1
        elif l2 > r1:
            a_start_k = cut_a + 1
        else:
            if total_len % 2 == 0:
                return (max(l1, l2) + min(r1, r2))/2
            else:
                return max(l1, l2)
    return -1

print(findMedianSortedArray([],[2,3]))
