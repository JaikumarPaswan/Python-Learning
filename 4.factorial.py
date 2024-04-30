# Recussive approach

# def fact(n):
#     if n == 0 or n == 1:
#        return 1
#     return n * fact(n-1)
       

# print(fact(5))

# Iterative approach

def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i

    return res

print(fact(5)) 