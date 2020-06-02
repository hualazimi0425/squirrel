# solution 1, Time complexity O(n), space complexity (n)

def spiralOrder(matrix):
    R = len(matrix)
    C = len(matrix[0])
    seen = [[False] * C for _ in matrix]
    result = []
    dr = [0, 1, 0, -1]
    # row direction associate with  right, down, left, top
    dc = [1, 0, -1, 0]
    # column direction associate with right, down,left, top
    r, c, direction = 0, 0, 0
    for _ in range(R * C):
        result.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[direction], c + dc[direction]
        if 0 <= cr < R and 0 < cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            direction = (direction + 1) % 4
            r, c = r + dr[direction], c + dc[direction]
    return result


# solution 2 concise and straightforward
def spiralOrder2(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    n = len(matrix)
    m = len(matrix[0])
    u, d, l, r = 0, n - 1, 0, m - 1
    while l < r and u < d:
        result.extend([matrix[u][j] for j in range(l, r)])
        result.extend([matrix[i][r] for i in range(u, d)])
        result.extend([matrix[d][j] for j in range(r, l, - 1)])
        result.extend([matrix[i][l] for i in range(d, u, - 1)])
        u, d, r, l = u + 1, d - 1, r - 1, l + 1
    if l == r:
        result.extend(matrix[i][r] for i in range(u, d + 1))
    elif u == d:
        result.extend(matrix[u][j] for j in range(l, r + 1))
    return result
