# def isPal(s):
#     i = 0
#     j = len(s)-1
#     for k in range(len(s)//2):
#         if s[i]!=s[j]:
#             return False
#         else:
#             i+=1
#             j-=1
        
#     return True

def isPal(s):
    low=0
    high=len(s)-1
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True


# def isPal(s):
#     return s==s[::-1]



print(isPal("kenek"))