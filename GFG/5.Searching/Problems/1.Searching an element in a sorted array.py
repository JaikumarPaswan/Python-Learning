def searchInSorted(arr, N, K):
        low = 0
        high = N-1
        while low<=high:
            mid = (low+high)//2
            
            if arr[mid]==K:
                return 1
            else:
                if arr[mid]>K:
                    high = mid - 1
                elif arr[mid]<K:
                    low = mid + 1
        return -1