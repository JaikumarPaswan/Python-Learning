def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
        
    return True

print(isprime(4))
        

