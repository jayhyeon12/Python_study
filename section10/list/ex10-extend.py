num_list = [1, 2, 3]

num_list.append(4)
print(num_list) # [1, 2, 3, 4]

ext_list = [5, 6, 7]
print(ext_list) # [5, 6, 7]

num_list.extend(ext_list)
print(num_list) # [1, 2, 3, 4, 5, 6, 7]
