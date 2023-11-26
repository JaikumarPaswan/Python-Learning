# def isPalindrome(str, start, end):
#     if start>=end:
#         return True
#     return (str[start]==str[end] and isPalindrome(str, start+1, end-1))

# str = "luaul"
# start=0
# end=4

# print(isPalindrome(str, start, end))




def ispal(str):
    start = 0
    end = len(str)-1
    while start<=end:
        if str[start]!=str[end]:
            return False
        start+=1
        end-=1
    return True


print(ispal("luaul"))