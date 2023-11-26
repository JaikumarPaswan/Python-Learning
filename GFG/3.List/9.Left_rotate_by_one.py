def rotate(l):
    first = l[0]
    l.remove(l[0])  #in one line-> l.append(l.pop(0))
    l.append(first)
    return l

l= [1,2,3,4]
print(rotate(l))

# def rotate(l):
#     l = l[1:] + l[0:1]
#     return l

# def rotate(l):
#     x = l[0]
#     n = len(l)
#     for i in range(1, n):
#         l[i-1] = l[i]
#     l[n-1]=x

#     return l
    

