def search(reader, target):
    if reader.get(0) == target:
        return 0
    # search boundaries
    left, right = 0, 1
    while reader.get(right) < target:
        left = right
        right = right * 2
    # binary search
    while left <= right:
        pivot = left + (right - left)//2
        nums = reader.get(pivot)
        if nums == target:
            return pivot
        if nums > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1 