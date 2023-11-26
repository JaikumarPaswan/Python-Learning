#Naive solution

# def sort(a, b):
#     c = a+b
#     c.sort()
#     return set(c)


# def sort(a, b):
#     c = a+b
#     c.sort()
#     for i in range(0, len(c)):
#         if(i==0 or c[i] != c[i-1]):
#             print(c[i], end=" ")

# a=[2,4,6,8,9]
# b=[2,2,4,5,6,6,9]
# print(sort(a,b))


#Efficient solution  θ(m+n) which is linear[m=len(a), b=len(b)]

def union(a,b):
    i=0
    j=0
    while (i<len(a) and j<len(b)):
        if(i>0 and a[i] == a[i-1]):
            i+=1
        elif (j>0 and b[j] == b[j-1]):
            j+=1
        elif a[i] > b[j]:
            print(b[j], end=" ")
            j+=1
        else:
            print(a[i], end=" ")
            i+=1
            j+=1

    while(i<len(a)):
        if(i>0 and a[i]!=a[i-1]):
            print(a[i], end=" ")
        i+=1
    while(j<len(b)):
        if(j>0 and b[j]!=b[j-1]):
            print(b[j], end=" ")
        j+=1


a=[2,4,6,8,9]
b=[2,2,4,5,6,6,9]
print(union(a,b))