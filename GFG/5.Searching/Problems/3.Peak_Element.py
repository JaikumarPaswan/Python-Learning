# O(n) solution
# def peak(arr, n):
    # if n == 1:
    #     return 0
    # elif arr[0]>=arr[1]:
    #     return 0
    # elif arr[n-1]>=arr[n-2]:
    #     return n-1
    
#     for i in range(n):
#         if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
#             return i
    

#Binary search solution, explanation by neet code(written by me)
# def peek(arr, n):
#     low = 0
#     high = n-1
#     while low<=high:
#         mid = (low+high)//2
#         if n == 1:
#             return 0
#         elif arr[0]>=arr[1]:
#             return 0
#         elif arr[n-1]>=arr[n-2]:
#             return n-1
                
#         if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:                return mid    
#         elif arr[mid]<arr[mid-1]:
#             high = mid-1
#         elif arr[mid]<arr[mid+1]:
#             low = mid + 1


def peak(arr):
    low = 0
    high = len(arr-1)
    while low<=high:
        mid = (low+high)//2
        #left neighbour greater
        if mid>=0 and arr[mid] < arr[mid-1]:
            high = mid-1
        
        #right neighbour greater
        elif mid < len(arr) - 1 and arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            return mid