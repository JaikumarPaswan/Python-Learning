def isRotated(s1, s2):
    if len(s1) != len(s2):
        return False
    
    # Concatenate s1 with itself
    concatenated = s1 + s1
    
    # Check if s2 is a substring of concatenated
    if s2 in concatenated:
        return True
    else:
        return False
        
print(isRotated("geek", "eekg"))

# s = "apple"
# n = s.strip(s[0])  #use strip to remove any index from string
# print(n)