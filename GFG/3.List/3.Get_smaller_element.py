def smaller(l, x):
    small =[]
    for i in l:
        if i< x:
           small.append(i)
    return small
        
l = [12, 43, 21, 4, 77, 80]
x = 50

print(smaller(l, x))