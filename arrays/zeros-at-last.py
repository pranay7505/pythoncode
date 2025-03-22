def zeroatlast(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count +=1

    return arr

arr = [12, 0, 55, 11, 0, 575, 0]

print(zeroatlast(arr))