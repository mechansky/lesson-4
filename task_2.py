basic_list = [1, 0, 2, 1, 2, 3, 2, 4, 3, 5, 4, 6]


new_list = [basic_list[element] for element in range(len(basic_list)) if basic_list[element] > basic_list[element - 1]]

print(new_list)