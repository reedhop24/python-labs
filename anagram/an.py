import time

# Naive solution

def is_anagram(a, b):
    return ''.join(sorted([char for char in a])) == ''.join(sorted([char for char in b]))

# Better solution

def is_anagram_two(a, b):
    def letters(string):
        letter_dict = {}
        for x in string:
            if x in letter_dict:
                count = letter_dict.get(x)
                count += 1
                letter_dict.update({x: count})
            else:
                letter_dict.update({x: 1})
        return letter_dict
    a_dict = letters(a)
    b_dict = letters(b)
    
    for y in a_dict.items():
        if y[0] in b_dict:
            if b_dict.get(y[0]) != y[1]:
                return False
        else:
            return False

    return True

print(is_anagram_two('hello', 'llohe'))
