def is_rotated(list_one, list_two):
    idx = list_two.index(list_one[0])
    for i in list_one:
        if i != list_two[idx]:
            return False
        idx = 0 if idx == len(list_two)-1 else idx+1
    return True


print(is_rotated([1,2,3,5,6,7,8], [6,5,7,8,1,2,3]))