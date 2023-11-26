#It takes less memory than other algorithm's
#Not Stable
#Inplace algorithm

#we found the smallest element and swap it with first element,
#next we find the next smallest element and swap it with 2nd element

def selectSort(l):
    n = len(l)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1, n):
            if l[j]<l[min_ind]:
                min_ind=j
        l[min_ind], l[i] = l[i], l[min_ind]

l = [11, 9, 6, 3, 5]
(selectSort(l))
print(l)