# m = int(input("Enter m:"))
# n = int(input("Enter n:"))

# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)

#     if (m%n)==0:
#         return(n)
#     else:
#         diff =m-n
#         return(gcd(max(n,diff),min(n,diff)))


# print(gcd(m,n))

first = "tarantula"
second = ""
for i in range(len(first)-1,-1,-1):
  second = first[i] + second

print(second)
