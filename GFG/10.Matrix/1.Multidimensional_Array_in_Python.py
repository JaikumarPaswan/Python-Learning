# arr = [[1,2,3],[4,5,6,7,8]]

# for r in arr:
#     for x in r:
#         print(x, end=" ")
#     print()

# print("Number of rows", len(arr))
# print("Count in the first rows", len(arr[0]))
# print("Count in the second row", len(arr[1]))


#An Alternate way of Traversal

# arr = [[1,2,3],[4,5,6,7,8]]

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end=" ")
#     print()



#User Specified Dimensions
rows = 3
cols = 4

#Not a Recommended way to create 2D array in python (see output)
# arr=[[0]*cols]*rows    #Due to internal memory optimisation, python uses same memory for all rows and due to this changes are refelected in every row
# arr[0][0] = 1
# for r in arr:
#     print(r)

arr = [[0 for i in range(cols)] for j in range(rows)] #always use this way to create 2-D array in python
arr[0][0] = 1
for r in arr:
    print(r)