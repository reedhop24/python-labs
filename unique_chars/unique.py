def unique_chars(string):
    char_dict = {}
    for x in string:
        if x in char_dict:
            return False
        else:
            char_dict.update({x : 0})
    return True

print(unique_chars('helo'))
print(unique_chars('hello'))