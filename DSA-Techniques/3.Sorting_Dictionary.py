my_dict = {2:3, 1:4, 5:1, 6:9, 4:3}


sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)