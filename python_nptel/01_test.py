# def max3bad(x,y,z):
#   maximum = 0
#   if x >= y:
#     if x >= z:
#         maximum = x
#     else: 
#         maximum = z

#   else:
#     if y>=z:
#         maximum = y
#     else:
#         maximum = z
    
#   return(maximum)

# m = max3bad(99,858,10)
# print(m)

# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3

# m = maximum(455, 86, 96)
# print(m)

# m = max3bad(10, 6, 95)
# print(m)


# import math

# def isprimebad(n):
#   if n < 2:
#     return(False)
#   else:
#     for i in range(2, int(math.sqrt(n))):
#       if n%i == 0:
#          return(False)
#     return(True)

# i = isprimebad(6001)
# print(i)