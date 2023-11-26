def power(x,n):
    res = 1
    for i in range(n):
        res = res*x
    
    return res

print(power(2,3))


def power1(x,n):
    return x**n

print(power1(2,3))