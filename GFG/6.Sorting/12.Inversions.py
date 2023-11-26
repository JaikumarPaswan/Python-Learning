#Navive approach:  TC- O(n**2)

# def inversion(a):
#     res=0
#     j=0
#     while len(a)!=0:
#         for i in range(len(a)):
#             if a[j]>a[i]:
#                 res+=1
#         del a[0]
    
#     return res

# def inversion(a):
#     n=len(a)
#     res = 0
#     for i in range(n-1):
#         for j in range(i + 1, n):
#             if a[i] > a[j]:
#                 res += 1
#     return res


# a = [5,4,3,2]
# print(inversion(a))


#Efficient soln

def mergeSort(arr, n):
	temp_arr = [0]*n
	return _mergeSort(arr, temp_arr, 0, n-1)

def _mergeSort(arr, temp_arr, left, right):

	inv_count = 0

	if left < right:

		mid = (left + right)//2

		inv_count += _mergeSort(arr, temp_arr,
								left, mid)

		inv_count += _mergeSort(arr, temp_arr,
								mid + 1, right)


		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count


def merge(arr, temp_arr, left, mid, right):
	i = left	 
	j = mid + 1 
	k = left	 
	inv_count = 0

	while i <= mid and j <= right:

		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]

	return inv_count


arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)
