#Most efficient in speed but not stable
# def hoarePartition(arr, l, h):
#     pivot = arr[l]
#     i=l-1
#     j=h+1
#     while True:
#         i=i+1
#         while arr[i]<pivot:
#             i=i+1

#         j=j-1
#         while arr[j]>pivot:
#             j=j-1

#         if i>=j:
#             return j
#         arr[i], arr[j]=arr[j], arr[i]


# def qSort(arr, l, h):
#     if l<h:
#         p = hoarePartition(arr, l, h)
#         qSort(arr, l, p)
#         qSort(arr,p+1,h)

# arr=[8,4,7,9,3,10,5]
# l=0
# h=6
# print(qSort(arr, l, h))
# print(arr)


def partition(arr,low,high):
        pivot=arr[low]
        i=low-1
        j=high+1
        while True:
            i=i+1
            while arr[i]<pivot:
                i=i+1
                
            j=j-1
            while arr[j]>pivot:
                j=j-1
                
            if i>=j:
                return j
            arr[i],arr[j]=arr[j],arr[i]
            
            
    
    
def quickSort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        quickSort(arr,low,p)
        quickSort(arr,p+1,high)



arr=[4,1,3,9,7]
low=0
high=4

print(quickSort(arr,low,high))
print(arr)