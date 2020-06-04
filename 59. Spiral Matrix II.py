def generateMatrix(n):
    m = [[0] * n for _ in range(n)]
    # initiate matrix
    i, j, di, dj = 0, 0, 0, 1
    # di, dj: direction of row, direction of column
    for k in range(n*n):
        m[i][j] = k + 1
        if m[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return m


print(generateMatrix(3))