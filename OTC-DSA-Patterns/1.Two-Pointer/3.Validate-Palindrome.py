#https://leetcode.com/problems/valid-palindrome/description/


import re




def isPalaindrome(s):
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9]', '', s) #r makes the string a raw string, so Python does not treat backslashes as escape characters.This ensures the regex pattern is passed to re.sub() exactly as written.It prevents bugs when using regex symbols like \d, \w, or \s."
    
    i=0
    j=len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True    


s = "A man, a plan, a canal: Panama"
print(isPalaindrome(s))


#Solution from a Leetcode user
# def isPalindrome(s):
#     new = []
#     for i in s:
#         if i.isalnum():  #is-alpha-numeric, checks and gives boolean value
#             new.append(i.lower())
#     return new == new[::-1]

