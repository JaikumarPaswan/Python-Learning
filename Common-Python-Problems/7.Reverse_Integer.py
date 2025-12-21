def reverse(x):
    isnegative = False

    if x<0:
        isnegative = True
        x=x*-1

    res = 0
    while x>0:
        d = x%10
        res = (res*10)+d
        x = x//10

    return res*-1 if isnegative else res


print(reverse(-123))
