# # Create a dictionary to store the counts of each element in the array
# array = [1, 2, 1, 3, 2, 4]

# counts = {}
# for num in array:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1

# print(counts)




#Given an array of integers: [1, 2, 1, 3, 2] and we are given some queries: [1, 3, 4, 2, 10]. For each query, we need to find out how many times the number 
# appears in the array. For example, if the query is 1 our answer would be 2, and if the query is 4 the answer will be 0. 

# Given array of integers
array = [1, 2, 1, 3, 2]

# Given queries 
queries = [1, 3, 4, 2, 10]



# Function to get the count of each query
def count_occurrences(array, queries):
    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    result_dict = {}
    for query in queries:
        result_dict[query] = counts.get(query, 0)
    return result_dict

# Get the results for each query
results = count_occurrences(array, queries)

# Print the results dictionary
print(results)


#---------------
#Find key by providing value

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# value_to_find = 2

# for k, v in my_dict.items():
#     if v == value_to_find:
#         print(k)
#         break

