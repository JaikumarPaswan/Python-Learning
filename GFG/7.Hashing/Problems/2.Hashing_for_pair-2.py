def pairExists(arr, N, sum):
    num_set = set()
    res=0
    
    for num in arr:
        difference = sum - num
        
        if difference in num_set:
            res+=1
            
        num_set.add(num)
        
        if res>=2:
            return 1
            
    return 0



arr=[1, 2, 3, 4]
sum=5
N=4

print(pairExists(arr,N,sum))