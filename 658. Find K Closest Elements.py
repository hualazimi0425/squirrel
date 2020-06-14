#solution
# f(i) = abs(arr[i] - x) vs i
# g(i) = f(i) <= f(i + k)
# since we want to find exactly k elements around x
# the first i in k-window, f(i) should be smaller
# or equal than f(i + k), otherwise, i + 1 should be
# in k-window instead of i
# So we want to find such i
def findClosestElements(arr, k, x):
    l, r = 0, len(arr) - k
    while l < r:
        m = l + (r - l) // 2  # m is the starting point of window of size k
        if x - arr[m] > arr[m + k] - x:
            # compare the opposite and bump up i
            l = m + 1
        else:
            r = m
    return arr[l:l + k]