#Given an array [(120,30), (100,20), (60,10)],representing the value(first element in pair) and 
# weight(second element in pair) of items, and an integer capacity representing the 
# maximum weight a knapsack can hold, determine the maximum 
# total value that can be achieved by putting items in the 
# knapsack. You are allowed to break items into fractions if necessary.

#Calculate ratio(value/weight) for every item
#sort in decreasing order

def fractionalKnapsack(W, arr):
    n = len(arr)

    costWeight = []

    for i in range(n):
        c, w = arr[i][0], arr[i][1]
        costWeight.append((c, w, c/w))

    costWeight = sorted(costWeight, key=lambda x:x[2], reverse=True)

    res=0

    for curr in costWeight:
        if curr[1]<=W:
            res+=curr[0]
            W -= curr[1]
        else:
            res += curr[0] * (W/curr[1])
            break

    return res


arr = [(120,30), (100,20), (60,10)]
W = 50

print(fractionalKnapsack(W, arr))
    
    

