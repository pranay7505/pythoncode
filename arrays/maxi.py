n = int(input("enter n:-"))
lt = []
for i in range(0, n):
    lt.append(int(input()))

# mx = 0
mn = 0

# for i in range(0, n):
#     if lt[i] > mx:
#         mx = lt[i]

for i in range(1, n):
    if lt[i] < mn:
        mn2 = lt[i]


# print(mx)
print(mn)

span = mx - mn
print("span is - ",span)