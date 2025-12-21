# https://leetcode.com/problems/top-k-frequent-elements/description/
# def topk(nums, k):
#     my_dict={}

#     for i in range(len(nums)):
#         my_dict[nums[i]] = my_dict.get(nums[i], 0)+1
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda item:item[1]))

#     return list(sorted_dict.keys())[-k:]

# print(topk([3,3,1,1,1,1,7,7,7,4,9,12], 2))



def topk(nums, k):
    my_dict = {}
    for number in nums:
        my_dict[number] = my_dict.get(number, 0)+1

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item:item[1])) #my_dict.items(): This returns a view object that displays a list of a dictionary's key-value tuple pairs.
                                                                         #key=lambda item: item[1]: This is a lambda function defining the sorting key. It extracts the second element of each tuple, which corresponds to the values.
                                                                         #Finally, dict() is used to convert the sorted list of key-value pairs back into a dictionary.
    return list(sorted_dict.keys())[-k:]

print(topk([3,3,1,1,1,1,7,7,7,4,9,12,4,3], 2))