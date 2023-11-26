#T.C:- O(n^2), Brute force approach by me

# def pair(arr,sum,N):
#     res=0
#     for i in range(N):
#         for j in range(N):
#             if i==j:
#                 continue
#             if arr[i]+arr[j]==sum:
#                 res+=1

#             if res==1:
#                 return 1
          
#     return 0


#Brute force approach
# def pair(arr,sum,N):
#     res=0
#     for i in range(0,N):
#         for j in range(i+1,N):
#             if arr[i]+arr[j]==sum:
#                 res+=1

#             if res==1:
#                 return 1
          
#     return 0


#Two pointer approach
#T.C = O(nlogn)+O(n)  #O(n) to sort
# def pair(arr, sum, N):
#     arr.sort()
#     l=0
#     r=N-1
#     while l<r:
#         current_sum = arr[l]+arr[r]

#         if current_sum==sum:
#             return 1
#         elif current_sum<sum:
#             l+=1
#         else:
#             r-=1

#     return 0


#Using Hash-Map
def pairExists(arr,sum,N):
    num_set = set()

    for num in arr:
        difference = sum - num

        if difference in num_set:
            return 1
        
        num_set.add(num)
    
    return 0





arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum=14
N=10

print(pairExists(arr,sum,N))