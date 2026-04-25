# 5. Two Sum (Sorted Input)
# Given a sorted array and a target sum, find two numbers such that they add up to the target. Return their indices Jor values.

def fun(arr, target):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==target:
            return(left, right)
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1

    return -1

arr=[1,4,5,7,9]
target = 12

print(fun(arr, target))
