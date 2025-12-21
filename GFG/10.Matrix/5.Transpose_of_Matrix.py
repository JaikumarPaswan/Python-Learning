# def transpose(mat):
#     N=len(mat)
#     temp=[[0]* N for i in range(N) ] 
#     for i in range(N):
#         for j in range(N):
#             temp[i][j]=mat[j][i]
#     for i in range(N):
#         for j in range(N):
#             mat[i][j] = temp[i][j]

#     return mat



#Efficient way, In place, one traversal
def transpose(mat):
    N = len(mat)
    for i in range(N):
        for j in range(i+1, N):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat



mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(transpose(mat))

