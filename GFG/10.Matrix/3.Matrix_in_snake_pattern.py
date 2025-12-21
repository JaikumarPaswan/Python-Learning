#T.C:- O(MxN)

def printSnake(mat):
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        if i%2==0:
            for j in range(N):
                print(mat[i][j], end = " ")
            print()
        else:
            for j in range(N-1, -1, -1):
                print(mat[i][j], end =" ")
            print()


mat = [[10,20],[30,40],[50,60]]
printSnake(mat)