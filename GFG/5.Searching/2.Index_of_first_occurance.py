# O(n)
# def fun(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1

# arr = [1,10,10,20,40]
# x = 20
# print(fun(arr,x))
        

# Binary search recursive

# def firstOccurenceRecursive(arr, low, high, x):
#     if(low>high):
#         return -1
#     mid=(low+high)//2
#     if(x>arr[mid]):
#         return firstOccurenceRecursive(arr, mid+1, high, x)
#     elif(x<arr[mid]):
#         return firstOccurenceRecursive(arr, low, mid-1, x)
#     else:
#         if(mid==0 or arr[mid-1]!=arr[mid]):
#             return mid
#         else:
#             return firstOccurenceRecursive(arr, low, mid-1, x)
        

    

# arr = [1,10,10,20,40]
# x = 10
# low = 0
# high = 4

# print(firstOccurenceRecursive(arr, low, high, x))

#MOST EFFICIENT iterative way

def firstOccurence(arr, n, x):
    low=0 
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid+1 
        elif(x<arr[mid]):
            high=mid-1 
        else: #mid==x
            if(mid==0 or arr[mid-1]!=arr[mid]):
                return mid 
            else:
                high=mid-1
    
    return -1

arr = [1,10,10,20,40]
n=len(arr)
x = 10

print(firstOccurence(arr,n,x))
