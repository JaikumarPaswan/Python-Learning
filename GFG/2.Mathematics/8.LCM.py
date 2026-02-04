# def lcm(a, b):
#     res = max(a, b)
#     while True:    #while True means an infinite loop. It will run forever unless you break or return We don’t know in advance how many times the loop should run We want the loop to stop only when a condition inside is met
#         if res%a == 0 and res%b == 0:
#             return res
#         res += 1

# print(lcm(40, 60))

# def lcm(a, b):
#     res = max(a, b)
#     while True:
#         if res % a == 0 and res % b == 0:
#             return res
#         res += max(a, b)

# print(lcm(40, 60))




# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)
#                           #Formula:- a*b=gcd(a,b)*lcm(a,b)
# def lcm(a, b):
#     return a*b // gcd(a, b)

# print(lcm(4, 6))
