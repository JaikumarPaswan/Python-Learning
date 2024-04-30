# TC -> θ(n)
# def getmax(l):
#     res = l[0]
#     for i in range(1, len(l)):
#         res = max(res, l[i])

#     return res


# def getSecMax(l):
#     if len(l)<=1:
#         return None
#     lar = getmax(l)
#     slar = None
#     for x in l:
#         if x != lar:
#             if slar == None:
#                 slar = x
#             else:
#                 slar = max(slar, x)
        
#     return slar

# l = [5, 10, 15, 20, 25, 30]
# print(getSecMax(l))

# Using max function
# def getSecMax(l):
#     lar = max(l)
#     count = l.count(lar)
#     for i in range(count):
#         l.remove(lar)

#     slar=max(l)
#     return slar

# l = [5, 10, 15, 20, 25, 30, 30, 30]
# print(getSecMax(l))


#Efficient sloution(one traversal)
def getSecMax(l):
    if len(l)<2:
        return None
    lar = l[0]
    slar = None
    
    for x in l[1:]:
        if x> lar:
            slar = lar
            lar = x
        elif x!= lar:
            if slar == None or slar < x:
                slar = x

    return slar

l = [5, 10, 15, 20, 25, 30, 30, 30]
print(getSecMax(l))