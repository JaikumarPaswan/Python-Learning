def printMatrix(mat):
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        for j in range(N):
            print(mat[i][j], end =" ")
        print()



mat = [[10,20],[30,40],[50,60]]
printMatrix(mat)