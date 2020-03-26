def sum_ten(arr):
    num_dict = set()
    for x in arr:
        if (10-x) in num_dict:
            return [10-x, x]
        else:
            num_dict.update({x})
    return -1

print(sum_ten([1,2,5,5]))