def even_odd(n):
    if n%2 == 0:
        print("given number is even")
    else:
        print("given number is odd")

    return n
n = int(input("enter the value"))
print(even_odd(n))