def GCDandLCM(A,B):
    GCD = 1

    for i in range(2, min(A,B)+1):
        if A%i==0 and B%i==0:
            GCD = i

    LCM = None
    d = max(A, B)
    while True:
        if d%A==0 and d%B==0:
            LCM = d
            break
        else:
            d += max(A, B)

    return (LCM , GCD)

    

  


print(GCDandLCM(9,12))