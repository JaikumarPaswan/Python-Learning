def fun(arr):
    if arr[0] == 0:
        return 0
    elif arr[-1] == 1:
        return len(arr)
    else:
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == 0:
                high = mid-1
                if arr[mid] == 1 and arr[mid+1]==0:
                    return mid + 1
            elif arr[mid] == 1:
                low = mid +1
                if arr[mid] == 1 and arr[mid+1]==0:
                    return mid + 1


arr = [1,1,1,1,0,1]
print(fun(arr))

            
