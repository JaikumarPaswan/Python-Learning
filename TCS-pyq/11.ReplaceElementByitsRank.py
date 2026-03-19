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

# Constraints:
# 1 <= N <= 10 ^ 5
# - 10 ^ 9 <= arr[i] <= 10 ^ 9

N = int(input().strip())

arr = list(map(int, input().split()))

print(arr)

arr.sort()
print(arr)