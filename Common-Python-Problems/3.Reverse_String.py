def reverse(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev


# def reverse(s):
#     return s[::-1]

print(reverse("geek"))





def reverse1(s):
    rev=""
    for i in range(len(s)-1, -1, -1):
        rev=rev+s[i]
    return rev
    
print(reverse1("geek"))