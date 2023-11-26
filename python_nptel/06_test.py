# def subsequence(l1,l2):
#     count = 0
#     for i in l1:
#        if i in l2:
#            l2.remove(i)
#            count += 1
#     if count == len(1):
#         return (True)
#     else:
#         return(False)


#Q7

# a = input()
# b=a
# l = []
# while a != "":
#     a = input()
#     l.append(a)
# for i in range(0, len(l)):
#     if l[i].find(b) != -1:
#         print(l[i])

#Q8

# def maxaggregate(l):
#     dic = {}
#     for i in l:
#         if i [0] in dic:
#             dic[i[0]] += i[1]
#         else:
#             dic[i[0]] = i[1]
#     m = max(list(dic.values()))
#     x=[]
#     for i in dic:
#         if dic[i] == m:
#             x.append(i)
#     return sorted(x)


#