def reverse(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev


# def reverse(s):
#     return s[::-1]




print(reverse("geek"))