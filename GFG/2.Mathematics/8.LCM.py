# def lcm(a, b):
#     res = max(a, b)
#     while True:
#         if res%a == 0 and res%b == 0:
#             return res
#         res += 1

#     return res

# print(lcm(4, 6))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
                          #Formula:- a*b=gcd(a,b)*lcm(a,b)
def lcm(a, b):
    return a*b // gcd(a, b)

print(lcm(4, 6))