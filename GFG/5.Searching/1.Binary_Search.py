#Iterative binary search

# def bsearch(l, x):
#     low = 0
#     high = len(l)-1
#     while low<=high:
#         mid = (low + high)//2
#         if l[mid]==x:
#             return mid
#         elif l[mid]<x:
#             low = mid+1
#         else:
#             high = mid - 1
#     return -1


# l = [1,2,3,4,5,6,7,8]
# x=5
# print(bsearch(l,x))


#Recursive binary search

def bsearch(l, x, low, high):
    mid = (low+high)//2
    if low<=high:

        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return bsearch(l, x, low, mid-1)
        else:
            return bsearch(l, x, mid+1, high)
        
    return -1

l = [1,2,3,4,5,6,7,8]
x=5
low = 0
high = 7

print(bsearch(l,x,low,high))