# T.C O(m*n)  [m and n are length of the strings]
# def isSubSeq(s1, s2):
#     res=[]
#     for i in range(len(s2)):
#         for j in range(len(s1)):
#             if s2[i]==s1[j]:
#                 res.append(j)

#     for i in range(1,len(res)):
#         if res[i-1]>res[i]:
#             return False
#     return True

# print(isSubSeq("abcd", "adc"))


# T.C O(m+n)
def isSubSeq(s1,s2):
    i,j=0,0
    while(i<len(s1) and j<len(s2)):
        if s1[i]==s2[j]:
            j=j+1
        i=i+1
    
    if j==len(s2):
        return True
    else:
        return False
    
print(isSubSeq("abcd", "adc"))


#Recursive way
# def isSubSeq(s1, s2, m, n):
#     if n==0:
#         return True
#     if m==0:
#         return False
#     if s1[n-1]==s2[m-1]:
#         return isSubSeq(s1, s2, m-1, n-1)
#     else:
#         return isSubSeq(s1, s2, m-1, n)
    

