def dsum(n):
    if n//10 == 0: #n<10 return n
        return n
    return dsum(n//10) + n%10


print(dsum(223))