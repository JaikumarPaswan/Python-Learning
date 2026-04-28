#Q) Even numbers with gap of 2 starting with 2, find missing number. If all missing numbers are present then then return next even number after the largest number

#1: If array is sorted 
# def fun(N, A):
#     for i in range(N-1):
#         if A[i]+2 == A[i+1]:
#             continue
#         else:
#             return A[i]+2
#     return A[N-1]+2 



#2: If array is not sorted

# def fun(N, A):
#     map={}
#     for x in A:
#         if x in map:
#             map[x]+=1
#         else:
#             map[x]=1
    
#     j=2
#     for i in range(N):
#         if j in map:
#             j+=2
#         else:
#             return j
#     return j


# N=6
# A=[2,4,6,8,10,12]

# print(fun(N,A))



#Element Values identical blocks
# def fun(N, A):
#     count = 0
#     i = 0
    
#     while(i<N):
#         currentValue = A[i]
#         length = 0

#         while i<N and A[i]==currentValue:
#             length+=1
#             i+=1

#         if length == currentValue:
#             count+=1

#     return count

# A=[2,3,3,3,2,2,6,4,4,4,4]
# N=11
# print(fun(N, A))




#4 Print numbers which occured only one in list

# def fun(A):
#     map={}
#     for x in A:
#         if x in map:
#             map[x]+=1
#         else:
#             map[x] = 1
    
#     for y in map:
#         if map[y]==1:
#             print(y, end=" ")

# A=[4,5,6,4,7,5,9]

# fun(A)





#5 Max odd freq - min even freq of a string letters

# def fun(S):
#     map={}

#     for i in range(len(S)):
#         if S[i] in map:
#             map[S[i]]+=1
#         else:
#             map[S[i]]=1
    
#     odd=0
#     even=max(map.values())

#     for value in map.values():
#         if value%2==0:
#             if value<even:
#                 even=value
#         else:
#             if value>odd:
#                 odd=value
        
#     return odd-even

# S="aaabbbccdddddd"
# print(fun(S))


# n = int(input())

# if n<=2:
#     print(n*2)
# else:
#     print((n*2) + (n-2)*2)


# def fun(n):
#     ans=1
#     for i in range(n):
#         ans=ans*(n-i)
#     return ans

# print(fun(5))


#"111011110111110"

# print(ord("A"))
# print(chr(65))



# class New:
#     def __init__(self, name, age, roll):
#         self.Name = name
#         self.Age = age
#         self.Roll = roll

# a=New('Jai', 12, 25)

# print(a.Name)

