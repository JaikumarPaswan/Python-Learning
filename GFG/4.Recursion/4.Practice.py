# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)
#     print(n)

# print(fun(3))

# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n)
#     fun(n-1)

# print(fun(3))



#Recursive funcion which returns logn (if 16 then its 2**4, 4 is output)

# def fun(n):
#     if n<=1:
#         return 0
#     else:
#         return 1 + fun(n//2)
    

# print(fun(16))



#Recursive funcion which returns reverse binary for a number

def fun(n):
    if n==0:
        return 0
    fun(n//2)
    print(n%2)

print(fun(13))

# def decimal_to_binary(n):
#     return bin(n).replace("0b","")

# print(decimal_to_binary(10))