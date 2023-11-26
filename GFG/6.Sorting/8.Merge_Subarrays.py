#mid is not necessary to be actually a middle element
#l<=m<h 
# !important:- as list is provided we are changing it inplace
def merge(a, low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
    m = len(left)
    n = len(right)
    i=0
    j=0
    k = low
    while i<m and j<n:
        if left[i]<=right[j]:  #Equal is used to maintain stability
            a[k] = left[i]
            k+=1
            i+=1
        else:
            a[k] = right[j]
            k+=1
            j+=1

    while i<m:
        a[k] = left[i]
        k+=1
        i+=1
    while j<n:
        a[k] = right[j]
        k+=1
        j+=1
    
    return a

a=[10,15,20,40,8,11,55]
low = 0
mid = 3
high = 6

print(merge(a, low, mid, high))


