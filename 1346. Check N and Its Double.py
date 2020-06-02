# solution 1
def checkIfExist(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] != arr[j] and arr[j] == 2 * arr[i]:
                return True

    return False


# solution 2
def checkIfExist2(arr):
    seen = set()
    for i in arr:
        if i * 2 in seen or (i % 2 == 0 and i//2 in seen):
            return True
        seen.add(i)
    return False


print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist2([10, 2, 5, 3]))
