# 1 to n

# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)
#     print(n)


# print(fun(12))



# n to 1
#program 1
def fun(n):
    if n == 0:
        return  #This will return none after 0
    print(n)
    fun(n-1)

print(fun(12))

#program2
# def fun(n):
#     if n == 0:
#         return 0  #This will return upto 0, None will not get printed 
#     print(n)
#     return fun(n-1)

# print(fun(12))