def sortArrayByParity(arr):
    i, j = 0, 0 # i only track even number, j track every element in the list
    n = len(arr)
    while j < n:
        if arr[j] % 2 == 0 and arr[i] % 2 != 0:
            arr[j], arr[i] = arr[i], arr[j] # swap
        if arr[i] % 2 == 0:
            i += 1
        j += 1
    return arr


print(sortArrayByParity([1,3,2,4]))