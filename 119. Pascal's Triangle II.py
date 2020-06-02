import math


# solution for Pascal's I
def getRow(rowNum):
    triangle = []
    for row_num in range(rowNum):
        row = [None for _ in range(row_num + 1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j] + triangle[row_num - 1][j - 1]
        triangle.append(row)
    return triangle


# space complexity is O(k^2)
print(getRow(5)[4])


# solution for Pascal's II
def getRow(rowNum):
    pascal = [None for _ in range(rowNum + 1)]
    for i in range(rowNum + 1):
        pascal[i] = math.factorial(rowNum)//(math.factorial(i)*math.factorial(rowNum - i))
    return pascal


print(getRow(4))
