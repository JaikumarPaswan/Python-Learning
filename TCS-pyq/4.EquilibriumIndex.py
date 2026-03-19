#2. Equilibrium Index of an Array
#Given an array, find an index such that the sum of elements on its left is equal to the sum of elements on its right.
#Return-1 if no such index exists.

arr=[10,20,5,3,2]

if len(arr)<=2:
    print(-1)
else:
    for i in range(1, len(arr)-1):
        left=sum(arr[0:i])
        right=sum(arr[i+1 : len(arr)])
        if left==right:
            print(i)
            break
    else:
        print(-1)