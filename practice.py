# class Solution:
#     def absolute(self, I):
#         if I<0:
#             return I*(-1)
        
#         return I
            
        
# solution = Solution()

# result = solution.absolute(-32)

# print(result)

# def getByIndex(arr,n,idx):
#     if idx<n:
#         return arr[idx]
    
#     return -1


# arr = [1,2,5]
# n = 3
# print(getByIndex(arr, n, 10))

# def fun(arr, size, index, element):
#     new_arr = arr[:index]
#     new_arr.append(element)
#     new_arr = new_arr + arr[index:]
#     arr.clear()
#     arr.extend(new_arr)

#     return arr

# arr = [1,2,3,4]
# size = 5
# index=4
# element=100


# print(fun(arr, size, index, element))

# arr = [1,2,3,4,5]
# ar = [1,2,3,4,5,6,7,]

# new = arr + ar[4:]
# print(new)


# def median(A,N):
        
#         A.sort()
        
#         ##Your code here
#         if N%2 == 0:
#                 x = (N//2)-1
#                 y = N//2
#                 median = (A[x] + A[y])//2
#         else:
#                 median = A[(N-1)//2]
                
#         return median
#         #If median is fraction then convert the median to integer and return
     
#     #Function to find mean of the array elements. 
      
# def mean(A,N):
#     mean = sum(A)//N
        
#     return mean

# A=[1,2,3,4,5,6]
# N=6

# print(median(A,N))
# print(median(A,N))

# def smallerThanX(arr,n,x):
        
#         small_elements=[]
#         for i in range(n):
#             if arr[i]<x:
#                 small_elements.append(arr[i])
     
#         return len(small_elements)
                

# arr = [2,3,4,1,5]
# n = 5
# x = 3

# print(smallerThanX(arr,n,x))

# def majorityWins(arr, n, x, y):
#         for i in range(n):
#             x_count = 0
#             if arr[i] == x:
#                 x_count = x_count+1
                
#             y_count = 0
#             if arr[i] == y:
#                 y_count = y_count + 1
                
#         if x_count>y_count:
#             return x 
#         elif y_count>x_count:
#             return y
#         else: 
#             return -1
                

# def majorityWins(arr, n, x, y):
#     x_count = arr.count(x)
#     y_count = arr.count(y)

#     if x_count>y_count:
#         return x 
#     elif y_count>x_count:
#         return y
#     else: 
#         return -1



# arr = [1,1,2,2,3,3,3,4,4,4,4,4,5]
# x = 3
# y = 4
# n = 13
# print(majorityWins(arr, n, x, y))



# def isSorted(arr,n):
#     for x in arr:
#         for i in range(1,n):
#             if x<=arr[i]:
#                 return 1
#             if x>=arr[i]:
#                 return 1
            
#         return 0

# def isSorted(arr,n):
#         if n < 2 :
#             return 1
#         else:
#             if arr[0] <= arr[1]:
#                 for i in range(1,n-1):
#                     if arr[i] > arr[i+1]:
#                         return 0
#                 else:
#                     return 1
#             elif arr[0] >= arr[1]:
#                 for i in range(1,n-1):
#                     if arr[i] < arr[i+1]:
#                         return 0
#                 else:
#                     return 1
    
# arr = [3,2,2,2,2,3,4,5,6,886,6,7]
# n = len(arr)

# print(isSorted(arr,n))


# def reverseArray(arr,n):
#     for i in range(n):
#         arr[i] = arr[n-i]
#         return arr
    



# arr = [1,2,3,4,5]
# n = len(arr)

# print(reverseArray(arr,n))

# def maxArea(height):
#     n = len(height)
#     for i in range(n):
        

# def maxArea(self, height):
        #BRUTE FORCE

        # res = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - 1)*min(height[l], height[r])
        #         res = max(res, area)
        
        # return res

        # LINEAR TIME SOLUTION O(n)
        # res = 0
        # l,r = 0, len(height)-1

        # while l<r:
        #     area = (r-l) * min(height[l], height[r])
        #     res = max(res, area)

        #     if height[l]<height[r]:
        #         l += r
        #     else:
        #         r -= 1

        #     return res


# def removeDuplicates(nums):
        # unique_list=[]
        # for i in range(len(nums)):
        #     if nums[i] in nums:
                  

        
        # return len(unique_list), nums

# nums=[1,1,1,2,2,3,4,4,4,4,4]

# print(removeDuplicates(nums))


# def removeElement(nums, val):
#         for x in nums:
#             if x == val:
#                 nums.remove(x)
#         n = len(nums)

#         return n



# nums=[1,1,2,3,4,4,4]
# val=1

# print(removeElement(nums, val))

# def searchInsert(nums, target):
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#             elif nums[i]> target:
#                 return i
#             elif nums[len(nums)-1]<target:
#                  return len(nums)
                
            
# nums = [1,3,5,6]
# target = 10

# print(searchInsert(nums, target))



# def plusone(digits):
#     n = len(digits)
#     if digits[n-1] != 9:
#         digits[n-1] += 1
#         return digits
#     elif digits[:] == 9:

#     else:
#         k = n-1
#         if digits[k] == 9:
#             digits.append(0) 
#             if digits[k-1] != 9:
#                 digits[k-1] += 1
#             else:
                



    


# digits = [1,3,5,6]

# print(plusone(digits))

# k = n-1
#         for i in range(n):
#             if digits[k] == 9:
#                 # digits[k+1] = 


# def printNos(N):
#         if N == 0:
#             return 1
#         printNos(N-1)
#         print(N)


# print(printNos(5))


# def printArrayRecursively(arr,n):
        
#         if n < 0:
#             return
#         printArrayRecursively(arr, n-1)
#         print(arr[n-1])
        
# arr = [1,2,3,4]
# n=4
# print(printArrayRecursively(arr,n))



# def fun(n):
#     if n==0:
#         return n
#     fun(n//10)
#     print(n)

# n=2229
# print(fun(n))


# def countDigits(n):
#     if n < 10:
#             return 0
#     return countDigits(n//10) + 1


# n = 4242
# print(countDigits(n))

# def fibonacci(n):
#         #code here
#         if n==0:
#             return 0
#         if n==1:
#             return 1
            
#         return fibonacci(n-1) + fibonacci(n-2)


# n=5
# print(fibonacci(n))

# def nCr(n,r):
#     if n==0 or r==0:
#         return 1
#     return ( (n * nCr(n-1,r)) // ( (n-r)* (nCr((n-r)-1,r)))*(r * nCr(n,r-1) ) )


# n=5
# r=2
# print(nCr(n,r))


# def isPalin(N):
#         string = str(N)
#         if len(string) <= 1:
#             return True
#         elif string[0] == string[len(string)-1]:
#             return isPalin(string[1:len(string)-1])
#         else:
#             return False

# n = 123321

# print(isPalin(n))

# def plusOne(digits):
#         string = str(digits)
#         plus1 = int(string)+1
#         digits.clear()
#         digits=[]
#         #for i in range len(plus1):
#        #     digits.append(plus1[i])

# x = [1,2,3]



# def plusOne(digits):
#         string = ""
#         for digit in digits:
#             string += str(digit)
#         number = int(string) + 1
#         ans = []
#         for digit in str(number):
#             ans.append(int(digit))
#         return ans



# digits = [1,2,3]
# string = ""
# for x in digits:
#         string += str(x)

# print(string)
# [1], 1 [0,0]
# [1], 0 [-1,-1]

#Input: nums = [5,7,7,8,8,10]
#target = 8

# def searchRange(nums, target):
#         index=[]
#         for i in range(len(nums)):
#                 if nums[i] == target:
#                         index.append(i)
#                         return [index[0],index[-1]]
                
#         return [-1,-1]
            

# nums = [5,7,7,8,8,10]
# target = 8
# print(searchRange(nums, target))



# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
 
#     else:
#         # Element is not present in the array
#         return -1
 
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 100 
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")


# def leftIndex (N, arr, X):
#     low = 0
#     high = N-1
#     while low<=high:
#         mid = (low+high)//2

#         if arr[mid]>X:
#             high = mid - 1
#         elif arr[mid]<X:
#             low = mid + 1
#         else:
#             if mid == 0:
#                 return mid
#             elif arr[mid]==X and arr[mid-1]!=X:
#                 return mid
#             else:
#                 high = high -1
        
#     return -1

# N = 7
# arr = [3, 3, 3, 3, 3,5,8]
# X = 3

# print(leftIndex (N, arr, X))

# table = [[]for x in range(4)]
# print(table)

# for i in range(0):
#     print('j')

# hash = [-1 for x in range(8)]
# print(hash)

# def fun(n):
#     sum = 0
#     for i in range(n+1):
#         sum = sum + i
#     return sum    

# print(fun(5))

# def count(n):
#     i = 0
#     while n>0:
#         n = n//10
#         i+=1
#     return i

# print(count(4569))      


# def pal_check(n):    
#     string = str(n)

#     for i in range(len(string)//2):
#         if string[i]!=string[-(i+1)]:
#             return False
#     return True  

# print(pal_check(9))


# def countzeros(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact = fact*i

#     res=0
#     while(fact%10==0):
#         res = res + 1
#         fact = fact//10
#     return res


# print(countzeros(5))


# def prime(n):
#     if n<=1:
#         return False
    
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True

# print(prime(33))


# def average(l):
#     sum = 0
#     for i in range(len(l)):
#         sum = sum+l[i]

#     return sum/len(l)

# print(average([2,4,6]))


# def separate(l):
#     even=[]
#     odd=[]
#     for x in l:
#         if x%2==0:
#             even.append(x)
#         else:
#            odd.append(x)
    
#     return even , odd
    
# print(separate([10,21,24]))


# def smallerthan(l,i):
#     smaller=[]
#     for x in l:
#         if x<i:
#             smaller.append(x)
#     return smaller

# print(smallerthan([12,3,5,8,18],7))


# def largest(l):
#     for x in range(len(l)-1):
#         if  l[x]>l[x+1]:
#             l[x],l[x+1]=l[x+1],l[x]

#     return l[-1]
             
# print(largest([10,5,20,8,9]))
             

# def issorted(l):
#     if len(l)<=1:
#         return True
    
#     for i in range(len(l)-1):
#         if l[i] > l[i+1]:
#             return False
        
#     return True     

# print(issorted([1,2,4,6,3]))


# def rotate(l):
#     if len(l)<=1:
#         return l
#     f = l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[len(l)-1] = f

#     return l

# print(rotate([10,20,30,40]))


# def index(l, i):
#         if 0<=i<=len(l): 
#             return l[i]
#         return -1

# print(index([1,2,3,4,5]))


# def abs_diff(l,num,diff):
#     i=0
#     for x in l:
#         if abs(num - x) <= diff:
#             i +=1
#     return i    

# print(abs_diff([12, 3, 14, 56, 77, 13],13,2))


# def del_shift(l,i):
#     for x in range(i,len(l)-1):
#         l[x]=l[x+1]
#     l[len(l)-1] = 0  
#     return l
    
# l = [1,2,3,4,5,6]

# print(del_shift(l,0)) 




# def subArraySum(arr, n, s):
#     prefixSum = {0:-1}
#     res = [-1]
#     currSum = 0
#     for i in range(len(arr)):
#         currSum += arr[i]
#         diff = currSum - s
#         if diff in prefixSum:
#             res = [prefixSum[diff] + 2, i + 1] 
#             break
#         if currSum not in prefixSum:
#             prefixSum[currSum] = i
#     return res

# l = [1,4,20,3,10,5]
# 3
# print(subArraySum(l,33))/

# def median(A,N):
        
#         A.sort()
#         if N%2==0:
#             return (A[N//2]+A[(N//2)-1])//2
#         else:
#             return A[N//2]
     
   
# def mean(A,N):
#     return sum(A)//N


# def majorityWins(arr, n, x, y):
#         xcount = 0
#         ycount = 0
#         for i in range(n):
#             if arr[i] == x:
#                 xcount +=1
#             elif arr[i] == y:
#                 ycount += 1
            
#         if xcount == ycount:
#             return min(x,y)
#         elif xcount>ycount:
#              return x
#         else:
#             return y
        
       

# arr = [1, 1, 2 ,2, 3 ,3 ,4 ,4, 4 ,4, 5]
# n = 11
# x = 4
# y = 5

# print(majorityWins(arr,n,x,y))


# def two_sum(list, t):
#     for i in range(len(list)-1):
#         for j in range(1,len(list)):
#             if list[i]+list[j]==t:
#                 return i,j
            
#     return False

# print(two_sum([2,7,11,15], 9))


# Accenture , i forgot that we can directly count len of string, after this the actual way
# N = int(input())
# count = 0
# for i in range(1,N+1):
#     list = []
#     string = str(i)
#     for j in range(len(string)):
#         list.append(string[j])
#     c = len(list)
#     if c%2!=0:
#         count +=1
#     list = [None]

# print(count)



# N = int(input())
# count = 0
# for i in range(1,N+1):
#     string = str(i)
#     c = len(string)
#     if c%2!=0:
#         count +=1
    
# print(count)


# def theSequence(n):
#     if n==0:
#         return 1
#     return n + n*(theSequence(n-1))


# def otn(N):
#     if N==0:
#         return 0
#     otn(N-1)
#     print(N, end=" ")

# print(otn(12))


# class Solution:
#     def printArrayRecursively(self,arr,n):
#         if n==0:
#             return
#         self.printArrayRecursively(arr,n-1)
#         print(arr[n-1], end=" ")

# instance = Solution()
# instance.printArrayRecursively([1,2,3],3)

# def sod(n):
#     if n<10:
#         return n
#     return sod(n//10) +n%10

# print(sod(123))

# class Solution:
#     def countDigits(self, n):
#         '''
#         :param n: given number
#         :return: count of digits of n.
#         '''
#         sum = 0
#         if n<10:
#             return 
#         sum+=1
#         self.countDigits(n//10)
#         return sum

# instance = Solution()
# instance.countDigits(190)

# def sum(l1,l2):
#     str1=""
#     str2=""
#     for i in range(1,len(l1)+1):
#         str1 = str1 + str(l1[-i])
#     for j in range(1,len(l2)+1):
#         str2 = str2 + str(l2[-j])
    
#     finalstr = str(int(str1) + int(str2))
#     result=[]

#     for k in range(1,len(finalstr)+1):
#         result.append(int(finalstr[-k]))

#     return result

# print(sum([2,4,3], [5,6,4]))


# def firstOccurance(l,x):
#     high = len(l)-1
#     low = 0

#     while low<=high:
#         mid=(high+low)//2
#         if l[mid]==x:
#             if mid==0 or l[mid-1]!=l[mid]:
#                 return mid
#             else:
#                 high = mid-1
#         elif l[mid]<x:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1

# print(firstOccurance([1,10,10,20,20,40], 20))


# def lastOccurance(l,x):
#     high = len(l)-1
#     low = 0

#     while low<=high:
#         mid = (low+high)//2
#         if l[mid]==x:
#             if mid==len(l)-1 or l[mid]!=l[mid+1]:
#                 return mid
#             else:
#                 low = mid+1
#         elif l[mid]<x:
#             low = mid-1
#         else:
#             high = mid-1
            
#         return -1

# print(lastOccurance([1,10,10,20,20,40], 200))



def Count1(arr):
    if arr[0]==1:
        return len(arr)
    
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2

        if arr[mid]==0:
            low = mid+1
        if arr[mid]==1:
            if arr[mid-1]==0:
                return len(arr)-mid
            else:
                high = mid-1
    return 0
    

print(Count1([0,0,0,0,1,1,1]))






