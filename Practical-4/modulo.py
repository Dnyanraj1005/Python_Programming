def modulo(n, d):
    
    
    div = n // d
    rem = n - d * div
   
    if (rem < 0 and d > 0) or (rem > 0 and d < 0):
        rem += abs(d)
    
    return rem

n = int(input("Enter the value of n: "))
d = int(input("Enter the value of d: "))

print(modulo(n, d))

