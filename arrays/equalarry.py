t=int(input())
for i in range(t):
    n = int(input())
    lt = []
    for i in range(0, n):
        lt.append(int(input()))

    

    mn = min(lt)

    

    sum = 0

    for i in lt:
        sum += i - mn

    print(sum)




