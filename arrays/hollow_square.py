def hollow_square(n, m): 
    k = []
    for i in range(n):
        k.append(n )
        for i in range(m):
            k.append("*"*m)
        

    return k

      
   


print(hollow_square(3, 3))

