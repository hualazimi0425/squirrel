from typing import List


def maxArea(height: List[int])  -> int:
    max_area = 0
    n = len(height)
    left, right = 0, n - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area



print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,3,2,5,25,24,5]))