# def fun(l, x):
#     i = 0
#     for j in range(len(l)):
#         if l[j] == x:
#             i = i+1
#     return i

# l = [1,10,10,20,40]
# x = 10
# print(fun(l,x))

#First Occurence
def firstOcc(l, x):
    low=0 
    high=len(l)-1
    while(low<=high):
        mid=(low+high)//2
        if(x>l[mid]):
            low=mid+1 
        elif(x<l[mid]):
            high=mid-1 
        else:
            if(mid==0 or l[mid-1]!=l[mid]):
                return mid 
            else:
                high=mid-1
    
    return -1


#Last O
def lastOcc(l, x):
    low = 0
    high = len(l) - 1
    while low<=high:
        mid = (low+high)//2
        if l[mid] > x:
            high = mid-1
        elif l[mid]<x:
            low = mid+1
        else:
            if mid == len(l)-1 or l[mid] != l[mid+1]:
                return mid
            else:
                low = mid+1

        return -1
    

#O(n)+O(n) = O(n) time
def countOcc(l,x):
    first = firstOcc(l,x)
    if first == -1:
        return 0
    else:
        return lastOcc(l, x) - first + 1
    

l = [1,10,10,20,40]
x = 10
print(countOcc(l,x))