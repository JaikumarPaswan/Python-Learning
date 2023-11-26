def findFloor(A,N,X):
        low = 0
        high = N-1
        while high<=low:
            mid = (low+high)//2
            if X < A[0] or X > A[-1]:
                return -1
            elif A[mid] == X:
                return mid -1 
            elif X<A[mid+1] and X>[mid] and mid != 0 and mid != N-1:
                 return mid
            else:
                 if X < A[mid]:
                      high = mid -1
                 elif X > A[mid]:
                      low = mid -1


A = [1,2,8,10,11,12,19]
N = 7
X = 5
print(findFloor(A,N,X))

