def getByIndex(arr,n,idx):
    if idx<n:
        return arr[idx]
    
    return -1


arr = [1,2,5]
n = 3
print(getByIndex(arr, n, 10))