#Q1
def fun(N, arr):
    i = 0
    j = N-1
    while i<j:
        while i<j and arr[i] != 0:     #Without the condition i < j, if the loop continues to execute while arr[i] != 0, but i never reaches j, 
            i+=1                       #it can lead to an infinite loop. Adding the condition i < j ensures that the loop terminates when i and j converge.
        while i<j and arr[j] == 0:
            j-=1
        arr[i], arr[j] = arr[j], arr[i]

        i+=1
        j-=1
    return arr

print(fun(8, [4,5,0,1,9,0,5,0]))


# zeros to end of an array. 
# def pushZerosToEnd(arr, n): 
#     count = 0 # Count of non-zero elements 
      
#     # Traverse the array. If element  
#     # encountered is non-zero, then 
#     # replace the element at index 
#     # 'count' with this element 
#     for i in range(n): 
#         if arr[i] != 0: 
              
#             # here count is incremented 
#             arr[count] = arr[i] 
#             count+=1
      
#     # Now all non-zero elements have been 
#     # shifted to front and 'count' is set 
#     # as index of first 0. Make all  
#     # elements 0 from count to end. 
#     while count < n: 
#         arr[count] = 0
#         count += 1
          
# # Driver code 
# arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
# n = len(arr) 
# pushZerosToEnd(arr, n) 
# print("Array after pushing all zeros to end of array:") 
# print(arr) 
