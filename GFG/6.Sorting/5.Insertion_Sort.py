#O(n^2) worst case
#In place and stable
#Used in practice forsmall arrays
#O(n) in best case

#working:-
#    It run a loop checking i with i-(1,2...) elements and place the number at its right position

def insertionSort(l):
    for i in range(1, len(l)):
        x=l[i]
        j=i-1
        while j>=0 and x<l[j]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=x


l = [11, 9, 6, 3, 5]
(insertionSort(l))
print(l)