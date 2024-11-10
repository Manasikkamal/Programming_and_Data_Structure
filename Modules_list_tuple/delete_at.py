def delete_at(list_num=[], idx=0):
    if idx >= 0 and idx < len(list_num):  
        del list_num[idx]
    return list_num
list_num = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(list_num, idx)
print(new_list)

