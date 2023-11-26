# def countD(arr):
#     set = set(arr)
#     return len(set)


# arr = [10,20,10,30,30,20]

# print(countD(arr))


def countD(arr, n):
    res=1
    for i in range(1,n):
        if arr[i] not in arr[0:i]:
            res+=1

    return res

arr = [10,20,10,30,30,20]
n=6

print(countD(arr,n))


