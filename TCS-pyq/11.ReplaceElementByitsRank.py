# Q - Replace Elements by Its Rank in the Array
# Problem Statement:
# You are given an array of N integers.
# Your task is to replace each element of the array with its rank in the array.
# The rank of an element is defined as its position in the array when the array is sorted in ascending order.
# If two elements are equal, they should be assigned the same rank.

# Input Format:
# The first line contains an integer N denoting the size of the array.
# The second line contains N space-separated integers representing the array elements.

# Output Format:
# Print N space-separated integers representing the rank of each element in the original array order.

#Sample Input
#7
#1 5 8 15 8 25 9

#sample Output
#1 2 3 5 3 6 4

# Constraints:
# 1 <= N <= 10 ^ 5
# - 10 ^ 9 <= arr[i] <= 10 ^ 9

N = int(input().strip())

arr = list(map(int, input().split()))



rank_map={}
rank=1
for num in sorted(arr):
    if num not in rank_map:
        rank_map[num]=rank
        rank+=1
print(rank_map)


for x in arr:
    print(rank_map[x], end=" ")
