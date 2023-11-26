def isSorted(l):
    if len(l)<=1:
        return True
    
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
        
    return True


# def isSorted(l):
#     i=1
#     while i<len(l):
#         if l[i-1] > l[i]:
#             return False
#         i = i+1

#     return True

l = [1,2,3]
print(isSorted(l))


# def issorted(l):
#     sl = sorted(l) # It will not modify the original list but if you write l.sort it will sort the original list
#                    # Same with reversed(l) and l.reverse
#     if sl == l:
#         return True
    
#     return False

