# 6. Transpose of a Matrix
# Given an N x M matrix, compute its transpose (rows become columns and columns become rows)

# x=[
#     [1,2],
#     [3,4],
#     [5,6]
# ]

# result = [[0]*len(x) for i in range(len(x[0]))]

# for i in range(len(x)):  #len(x) above is 3 which is len of rows
#     for j in range(len(x[0])):  #len(x[0]) above is 2 is len of columns
#         result[j][i] = x[i][j]  #⭐Remember putting [i] before [j] here will give error

# print(result)


#Solving using list comprehension

# x=[
#     [1,2],
#     [3,4],
#     [5,6]
# ]

# T =[ [x[i][j] for i in range(len(x))] for j in range(len(x[0]))]

# print(x)



# Take input for rows and columns
n, m = map(int, input().split())

# Take matrix input
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Create transpose matrix
transpose = [[0]*n for _ in range(m)]

# Fill transpose
for i in range(n):
    for j in range(m):
        transpose[j][i] = matrix[i][j]

# Print transpose
for row in transpose:
    print(*row)