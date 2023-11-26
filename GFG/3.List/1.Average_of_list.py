def average(l):
    sum = 0
    for i in range (len(l)):
        sum = sum + l[i]

    return sum/len(l)


l=[10,20, 30]

print(average(l))

# def average(l):
#     sum = 0
#     for x in l:
#         sum = sum + l[x]

#     return sum/len(l)


# Library methods
# def average(l):
#     return sum(l)/len(l)
