#Q1
# def f(x):
#     d=0
#     while x >= 1:
#         (x,d) = (x/7,d+1)
#     return(d)

# print(f(3456))

#Q2
# def h(n):
#     s = 0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+i
#     return(s)

# x = (h(60)-h(45))  
# print(x) 

#Q3
# def g(m,n):
#     res = 0
#     while m >= n:
#         (res,m) = (res+1,m/n)
#     return(res)

# print(g(375,4))
    
#Q4
# def mys(m):
#   if m == 1:
#     return(1)
#   else:
#     return(m+mys(m-1))


#Week2

#Q1
# x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
# y = x[0:6]                     # Statement 2
# z = x                          # Statement 3
# w = y                          # Statement 4
# x[1] = x[1][0:3] + 'd'         # Statement 5
# y[2] = 4                       # Statement 6
# z[1][1:3] = 'yzw'              # Statement 7
# z[0] = 0                       # Statement 8
# w[4][0] = 1000                 # Statement 9
# a = (x[4][1] == 4)             # Statement 10

#Q2
# x = [423,'b',37,'f']
# u = x[1:]
# y = u
# w = x
# u = u[0:]
# u[1] = 53
# x[2] = 47

#Q3
# first = "tarantula"
# second = ""
# for i in range(len(first)-1,-1,-1):
#   second = first[i] + second

#Q4
# def mystery(l):
#   l = l[0:5]
#   return()

# list1 = [44,71,12,8,23,17,16]
# mystery(list1)

# print(mystery(1))

# def threesquares(m):
#   bank=[7, 15, 23, 28, 31, 39, 47, 55, 
#         60, 63, 71, 79, 87, 92, 95, 103, 
#         111, 112, 119, 124, 127, 135, 143,
#         151, 156, 159, 167, 175, 183,
#         188, 191, 199, 207, 215, 220, 
#         223, 231, 239, 240, 247, 252, 255]  
#   return(m not in bank)


# def repfree(s):
#   return(len(s)==len(set(s)))

# def hillvalley(l):
#     dec = False
#     inc = False
#     c = 0
#     for i in range(len(l)-1):
#         if c > 1:
#             return False
#         right = l[i+1]
#         middle = l[i]
#         diff = right - middle
#         if diff > 0:
#             if dec:
#                 c += 1
#             inc = True
#             dec = False
#         elif diff < 0:
#             if inc:
#                 c += 1
#             dec = True
#             inc = False
#     if c == 1:
#         return True
#     return False

# threesquares()

#week4 quiz
# def mystery(l,v):
#   if len(l) == 0:
#     return (v)
#   else:
#     return (mystery(l[:-1],l[-1]+v))

# triples = [ (x,y,z) for x in range(2,4) for y in range(2,5) for z in range(5,7) if 2*x*y > 3*z ]
# print(triples)

actor = {}
actor[["Star Wars", "Rey"]] = "Ridley"