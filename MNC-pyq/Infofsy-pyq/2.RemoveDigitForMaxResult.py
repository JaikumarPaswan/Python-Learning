#https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

def maxResult(number, digit):
    ans=[]

    for i in range(len(number)):
        if number[i]==digit:
            t = number[0:i] + number[i+1:len(number)]
            ans.append(t)
    return max(ans)


print(maxResult("123", "3"))