# def fun(l):
#     length = len(l)
#     if l[0] == 1:
#         return length
#     else:
#         for i in range(length):
#             if l[i] == 1:
#                 return length - i
#     return 0
            

# l = [0,0,0,1,1,1,1]

# print(fun(l))

#Binary search
def Count(arr):
    if arr[0]==1:
        return len(arr)
    
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2

        if arr[mid]==0:
            low = mid+1
        elif arr[mid]==1:
            if arr[mid-1]==0:
                return len(arr)-mid
            else:
                high = mid-1
    return 0
    

print(Count([0,0,1,1,1,1]))