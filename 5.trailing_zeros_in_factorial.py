# Naive way

# def countzeros(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact = fact*i

#     res=0
#     while(fact%10==0):
#         res = res + 1
#         fact = fact//10
#     return res

# print(countzeros(5))

# Efficient way
def countzeros(n):
    res = 0
    i = 5
    while (i<=n):
        res = res + n//i
        i=i*5
    return res

print(countzeros(5))