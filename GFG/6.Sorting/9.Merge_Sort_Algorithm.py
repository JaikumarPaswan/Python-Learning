#T.C:-  O(nlogn) 
#Aux-S :- O(n)

def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]

            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if r > l:
        m = (r + l) // 2
        mergeSort(arr, l, m)  #recursively call for left-half
        mergeSort(arr, m + 1, r)  #recursively call for right-half
        merge(arr, l, m, r)  #apply merge with sorting


arr = [10, 5, 30, 15, 7]

mergeSort(arr, 0, 4)
print(*arr)
