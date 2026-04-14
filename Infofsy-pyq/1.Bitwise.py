# Wael is well-known for how much he loves the bit-wise XOR operation, 
# while Kaito is well known for how much he loves to sum numbers, 
# so their friend Resli decided to make up a problem that would enjoy 
# both of them. Resli wrote down an array A of length N, an integer K 
# and he defined a new function called Xor-sum as follows:

# Xor-sum(x) = (x XOR A[1])+(x XOR A[2])+(x XOR A[3])++(x XOR A[N])

# Can you find the integer x in the range [0,K] with the maximum Xor-sum (x) value?
# Print only the value.

# Input format:
# The first line contains integer N denoting the number of elements in A.
# The next line contains an integer, k, denoting the maximum value of x.
# Each line i of the N subsequent lines(where 0 <= i <= N ) contains an integer describing Ai.

# Sample Input:
# n = 3
# k = 7
# array = [1, 6, 3]

# Sample Output: 14

def Xor_sum(k, arr):
    xorSum = sum(arr)

    for i in range(1, k+1):
        s = 0
        for j in arr:
            s += i ^ j
        if s > xorSum:
            xorSum = s
    return xorSum 

n = 4
k = 9
arr = [7, 4, 0, 3]
print(Xor_sum(k, arr))
