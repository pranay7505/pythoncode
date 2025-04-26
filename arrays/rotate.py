def rotateArr(lt):
    while i < j:
        lt[j], lt[i] =  lt[i], lt[j]
        i +=1
        j -= 1
    return lt






n = int(input("enter the n:"))
k = int(input("enter the k:"))
lt = []
j = n-1
i = 0
for i in range(0, n):
    lt.append(int(input()))

print(rotateArr(lt))

