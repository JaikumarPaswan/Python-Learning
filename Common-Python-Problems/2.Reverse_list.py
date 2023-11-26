def reverse(l):
    i = 0
    j = len(l)-1

    while i<j:
        l[i],l[j] = l[j],l[i]
        i+=1
        j-=1

    return l

print(reverse([10,20,30,40,50]))

