#Naive
#Advantage is that it's Stable among all partition algorithms


def partition(a,p):
    n = len(a)
    a[p], a[n-1] = a[n-1], a[p]
    temp=[]
    for x in a:
        if x<=a[n-1]:
            temp.append(x)
    for x in a:
        if x>a[n-1]:
            temp.append(x)
    for i in range(len(a)):
        a[i]=temp[i]
    
    return a

a=[5,13,6,9,12,8,11]
p=4                  #any number smaller than 4th index goesto left of it and bigger will go to right
print(partition(a,p))

        
                


        

