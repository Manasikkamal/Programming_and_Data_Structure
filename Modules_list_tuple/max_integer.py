def max_integer(my_list=[]):
    if not my_list: 
        return None

    max_val = None
    for num in my_list:
        if max_val is None or num > max_val:
            max_val = num

    return max_val

list_num = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(list_num)
print("Max: {}".format(max_value))
