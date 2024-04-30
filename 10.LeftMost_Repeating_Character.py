def leftMost(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                return i
    return -1


print(leftMost("bullut"))
            