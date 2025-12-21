# #O(n^2)

# def countFreq(arr,n):
#     for i in range(n):
#         flag=False               #this part checks ifseen before
#         for j in range(i):
#             if arr[i]==arr[j]:
#                 flag=True
#                 break

#         if flag==True:           #If seen ignore
#             continue

#         freq=1                    #If not seen before count frequency
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 freq+=1
#         print(arr[i],freq)




# def countFreq(arr,n):
#     hmp=dict()
#     for i in range(n):
#         if arr[i] in hmp.keys():
#             hmp[arr[i]]+=1
#         else:
#             hmp[arr[i]]=1

#     return hmp


#More Easy
def countFreq(arr, n):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return counts



arr=[10,20,20,30,10]
n=5

print(countFreq(arr,n))