# def intersection(a, b):
#     res = []
#     for x in a:
#         for y in b:
#             if x==y:
#                 res.append(x)
#     return set(res)


# def intersection(a,b):
#     for i in range(len(a)):
#         if i>0 and a[i-1]==a[i]:
#             continue
#         for j in range(len(b)):
#             if a[i] == b[j]:
#                 print(a[i], end=" ")
#                 break

           
# a = [3,5,10,10,10,15,15,20]
# b = [5,10,10,15,30]
# print(intersection(a, b))


def intersection(a,b):
    i=0
    j=0
    while i<len(a) and j<len(b):
        if i>0 and a[i]==a[i-1]:
            i+=1
            continue
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        elif a[i]==b[j]:
            print(a[i], end =" ")
            i+=1
            j+=1


a = [3,5,10,10,10,15,15,20]
b = [5,10,10,15,30]
print(intersection(a, b))   

