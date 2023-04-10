list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 11, 89]

count = {}

for element in list:
    if element in count:
        count[element] += 1
    else:
        count[element] = 1

print("Printing count of each item", count)
