def non_repeat(string):
    char_dict = {}
    for x in string:
        if x in char_dict:
            count = char_dict.get(x)
            count += 1
            char_dict.update({x: count})
        else:
            char_dict.update({x: 1})

    for i in char_dict.items():
        if i[1] == 1:
            return i[0]


print(non_repeat('heelloo'))