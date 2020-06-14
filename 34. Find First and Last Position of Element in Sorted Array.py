def searchRange(nums, target):

    def lowerBound(nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l
    def upperBound(nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return l
    if not nums:
        return [-1, -1]
    lower = lowerBound(nums, target)
    upper = upperBound(nums, target)
    return [lower, upper] if lower <= upper - 1 else [-1, 1]