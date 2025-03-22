n = int(input("Enter n: "))
lt = []

# Taking input from the user
for i in range(n):
    lt.append(int(input()))

# Reversing the list manually
i = 0
j = n - 1  # Last index
while i < j:  # Swap only till the middle
    lt[i], lt[j] = lt[j], lt[i]  # Pythonic swap
    i += 1
    j -= 1

print("Reversed List:", lt)
