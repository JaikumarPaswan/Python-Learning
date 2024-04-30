# #T.C O(n^2)
# def leftMostNonRepeatingCharacter(s):
#     for i in range(len(s)):
#         for j in range(i+1,len(s)):
#             if s[i]==s[j]:
#                 break
#             elif j==len(s)-1:
#                 return i
#     return -1

# print(leftMostNonRepeatingCharacter("geeksforgeeks"))


#T.C: O(n)  S.C: O(1)  
def nonRep(str):
    count=[0]*256

    for i in str:
        count[ord(i)]+=1

    for i in range(len(str)):
        if count[ord(str[i])] == 1:
            return i
        
    return -1

print(nonRep("geeksforgeeks"))


