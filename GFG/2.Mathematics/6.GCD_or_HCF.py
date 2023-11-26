# def gcd(a, b):
#     if a == b:
#         print(f"{a} is the GCD")
#     elif a > b:
#         x = []
#         for i in range(1, b + 1):
#             if b % i == 0 and a % i == 0:
#                 x.append(i)
#         print(f"The GCD is {max(x)}")
#     else:
#         x = []
#         for i in range(1, a + 1):
#             if a % i == 0 and b % i == 0:
#                 x.append(i)
#         print(f"The GCD is {max(x)}")
            

# print(gcd(15, 12))

# Euclidean Algorithm

# def gcd(a,b):
#     while a != b:
#         if a>b:
#             a = a-b
#         else:
#             b = b-a
#     return a

# print(gcd(12, 15))

# Optimised Euclidean Algorithm
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

print(gcd(12, 15))
        
