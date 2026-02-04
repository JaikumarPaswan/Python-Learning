def isPal(n):
    string = str(n)
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            print("No")
            return
    print("Yes")

    
        
    

print(isPal(789987))

# def isPal(n):
    
#     rev = 0
#     temp = n

#     while temp != 0:
#         id = temp %10
#         rev = rev * 10 + id
#         temp = temp // 10
#     return rev == n

# print(isPal(4554))



