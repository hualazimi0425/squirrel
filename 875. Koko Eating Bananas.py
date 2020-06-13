def minEatingSpeed(piles, H):
    """
    :type piles: List[int]
    :type H: int
    :rtype: int
    """

    def possible(piles, k, H):
        return sum(int((pile - 1) / k) + 1 for pile in piles) <= H

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(piles, mid, H):
            hi = mid
        else:
            lo = mid + 1
    return lo
print(minEatingSpeed([3, 6, 7, 11], 8))