def compare_lists(list_one, list_two):
    elements = []

    for x in list_one:
        if x in list_two:
            elements.append(x)

    return elements

print(compare_lists([101,81,1,2,3,4,69,72], [7,1,2,5,3,9,10,4]))

