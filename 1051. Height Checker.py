def heightChecker(heights):
    heights_s = sorted(heights)
    diff = [heights[i] - heights_s[i] for i in range(len(heights))]
    return len(list(filter(lambda x: x != 0, diff)))


print(heightChecker([1, 1, 4, 2, 1, 3]))
