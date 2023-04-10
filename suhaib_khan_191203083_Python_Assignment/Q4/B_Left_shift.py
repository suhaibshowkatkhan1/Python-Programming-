def shift_left(lst):
    return lst[1:] + [lst[0]]


print(shift_left([1, 2, 3]))
print(shift_left([11, 12, 13]))
