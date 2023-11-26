# def separate(l):
#     even=[]
#     odd=[]
#     for i in range(len(l)):
#         if l[i] % 2 == 0:
#             even.append(l[i])
#         else:
#             odd.append(l[i])

#     return even, odd
    

def separate(l):
    even=[]
    odd=[]
    for x in l:  # This line takes values in list sequently
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    return even, odd

l = [1,2,3, 4, 5, 6, 8, 9]
print(separate(l))


