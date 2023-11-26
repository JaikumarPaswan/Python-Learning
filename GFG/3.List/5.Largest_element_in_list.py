#T.C -> O(n)

# def getmax(l):
#     for x in l:
#         for y in l:
#             if y>x:
#                 break
#         else:          # else is written with for loop
#             return x
#     return None
            

# l = [10, 30, 44, 21, 87]
# print(getmax(l))

# T.C ->  θ(n)
def getmax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i]>res:
                res = l[i]

    return res

l = [10, 30, 44, 21, 87]
print(getmax(l))
