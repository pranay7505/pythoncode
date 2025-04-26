def generate_square(n):
    for i in range(n):
        print("*" * n )
    return [generate_square]


n = int(input("enter n : "))
print(generate_square(n))