from bisect import bisect
from typing import List
import heapq
def kthSmallest1(matrix:List[List[int]], k: int) -> int:
    # the size of the matrix
    n = len(matrix)
    # preparing our min-heap
    minHeap = []
    for r in range(min(k, n)):
        minHeap.append((matrix[r][0], r, 0)) # we add triplets of information for each cell
    heapq.heapify(minHeap)   #heapify our list
    while k:  # until we find k elements
        # extra min
        element, r, c = heapq.heappop(minHeap)
        # if we have any new elements in the current row, add them
        # we removed row r, column c element, so the next element
        # need to be pushed in the heap is matrix[r][c+1] if exists
        if c < n - 1:
            heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        # decrement k
        k -= 1
    return element

# solution: binary search
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    m = len(matrix[0])
    l, r = matrix[0][0], matrix[n - 1][m - 1]
    while l < r:
        count = 0
        mid = l + (r - l)//2
        if sum(bisect(row, mid) for row in matrix) < k:
            l = mid + 1
        else:
            r = mid
    return l

print(kthSmallest1([[ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]], 8))

print(kthSmallest([[ 1,  5,  9],
   [2, 3, 10],
   [12, 13, 15]], 8))