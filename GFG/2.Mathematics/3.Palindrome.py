# def isPal(n):
#     string = str(n)
#     if len(string) == 1:
#         print("yes")
#     else:
#         for i in range(len(string)//2):
#             start = string[i] 
#             end = string[len(string)-1-i]
#         if (start == end):
#             print("yes")
#         else:
#             print("No")

#     return 

# print(isPal(789987))

def isPal(n):
    
    rev = 0
    temp = n

    while temp != 0:
        id = temp %10
        rev = rev * 10 + id
        temp = temp // 10
    return rev == n

print(isPal(4554))

