def most_frequent(arr):
    num_dict = {}
    maximum = 0
    for x in arr:
        if x in num_dict:
            count = num_dict.get(x)
            count += 1
            if count > maximum:
                maximum = x
            num_dict.update({x: count})
        else:
            if maximum < 1:
                maximum = x
            num_dict.update({x: 1})

    return maximum

print(most_frequent([1,2,2,2,3,3,4]))