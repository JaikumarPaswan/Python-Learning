#1. First Non-Repeating Character
#Given a string, find the first character that does not repeat. If none exists, print-1.

#s="ababcdcf"

s=input()

map={}
for x in s:
    if x in map:
        map[x]+=1
    else:
        map[x]=1


for j in s:
    if map[j]==1:
        print(j)
        break
else:
    print(-1)

# 🔎 Why iterate over s instead of map?
# Because:

# Dictionary preserves insertion order (Python 3.7+)

# But safer and more correct to check in original string order



#Another way using a Flag
# s=input()
# freq = {}

# for x in s:
#     if x in freq:
#         freq[x] += 1
#     else:
#         freq[x] = 1

# found = False

# for ch in s:   # iterate original string to preserve order
#     if freq[ch] == 1:
#         print(ch)
#         found = True
#         break

# if not found:
#     print(-1)

# not is a logical operator that reverses (negates) a Boolean value. [ps: we can use if found==false: print(-1)]

# Value	not value
# True	False
# False	True









