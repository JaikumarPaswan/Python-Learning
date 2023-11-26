# A = [1,2,3,4,5,6]
# N = 6
# if N%2 == 0:
#         x = (N//2)-1
#         y = N//2
#         median = A[x] + A[y]
# else:
#         median = A[(N-1)//2]
                
# N = 6
# x = (N//2)-1
# y = N//2

# print(N)
# print(x)
# print(y)

# A = [1,2,3,4,5,5,5,5,6]

# x = 5
# for x in A:
#      A.remove(x)

# print(A)


# def searchInSorted(arr, N, k):
#         low = 0
#         high = N-1
#         while low<=high:
#             mid = (low+high)//2
            
#             if arr[mid]== k:
#                 return 1
#             else:
#                 if arr[mid]>k:
#                     high = mid - 1
#                 elif arr[mid]<k:
#                     low = mid + 1
#         return -1

# arr = [1,10,10,20,40]
# k = 1

# print(searchInSorted(arr, 5, k))

# def inversion(a):
#     res = 0
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             if a[i] > a[j]:
#                 res += 1
#     return res

# a=[5,4,3,2]

# print(inversion(a))

# def binSort(A):
#         zero=[]
#         one=[]
#         for x in A:
#             if x==0:
#                 zero.append(x)
#             else:
#                 one.append(x)
                
#         A = zero+one
#         return A

# A=[1,0,1,1,0]

# print(binSort(A))


# def binSort(A, N):
#         j=0
#         for i in range(N):
#             if A[i]==0:
#                 A[i],A[j]=A[j],A[i]
#                 j+=1
                
#         return A

# A=[1,0,1,1,0]
# N=5
# print(binSort(A,N))