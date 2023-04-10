list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_list_of_lists = []

for lst in list_of_lists:
    if lst not in unique_list_of_lists:
        unique_list_of_lists.append(lst)

print(unique_list_of_lists)
