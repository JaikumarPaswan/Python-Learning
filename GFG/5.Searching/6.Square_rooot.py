# O(n)
# def fun(x):
#     i = 1
#     while i*i<=x:
#         i+=1
#     return i-1


def sqrootfloor(x):
    low = 1
    high = x
    ans = -1
    while low<=high:
        mid = (low+high)//2
        msq = mid * mid
        if msq == x:
            return mid
        elif msq>x:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans

print(sqrootfloor(10))