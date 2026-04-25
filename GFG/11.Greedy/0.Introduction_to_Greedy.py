#Greedy algorithms are mainly useful for Optimization Prolems. An optimizing problem is maximizing or minimizing something eg.Shortest path.

#Q)Consider infinite supply of the following value of coins 10, 5, 2, 1
#If someone asks for an amount, how will you give this amount using minimum coins?
#Amount:52
#Take 5 coin of 10rs
#Take 1 coin of 2rs

def minCoins(coins, amount):
    coins.sort(reverse=True)
    res=0    
    for x in coins:
        if x<=amount:
            c=amount//x
            amount-=c*x
            res+=1
        if amount==0:
            break
    return res

amount=57
coins=[5,10,2,1]

print(minCoins(coins, amount))


#General structure of Greedy Algorithms
# def getOptimal(arr):
#     res=0
#     while(All Items are not considered):
#         i=selectItem()
#         if(feasible(i)):
#             res=res+i
#     return res



#Greedy algotithms may not work always
#consider
#coins=[18,10,1]
#amount=20
#With greedy answer=3 {18+1+1}
#Correct answer=2 {10+10}
#Greedy works fine with usual value of coins, but fails when provided random value of coins like 18


#Another example problem: Longest Path

#        ↱10[]2[]1⤵
# source-> 1[]20[]5 destination ⤴
#        ↳ 2[]5 ⤴

#With greedy, the top path is longest but in actual, the middle path is longest



#Applications
# A)Finding Optimal Solutions
#     Activity selection
#     Fractional Knapsack
#     Job Sequencing
#     Prim's Algorithm
#     Kruskal's Algorithm
#     Dijkstra's Algorithm
#     Huffman Coding
#
# B)Finding close to optimal solutions for NP Hard problems like 
# Travelling Salesman Problem.