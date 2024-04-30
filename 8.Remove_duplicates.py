# def rd(l):
#     unique_list = []
    
#     # Iterate over the list indices using the range function
#     for i in range(len(l)):
#         # Check if the current element is not already in the unique list
#         if l[i] not in unique_list:
#             unique_list.append(l[i])
    
#     return unique_list


# l = [10,10,10,20,40]
# print(rd(l))


# def remove_duplicates(sorted_list):
#     if not sorted_list:
#         return sorted_list  # Empty list has no duplicates

#     i = 0  # Pointer at the start
#     for j in range(1, len(sorted_list)):
#         if sorted_list[i] != sorted_list[j]:
#             i += 1
#             sorted_list[i] = sorted_list[j]

#     # The unique elements are now at indices 0 to left (inclusive)
#     return sorted_list[:i + 1]

# print(remove_duplicates([1,2,2,2,3,4,4,5]))


