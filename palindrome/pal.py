def is_palindrome(a):
    return a == ''.join(reversed([char for char in a]))
    
def is_palindrome_two(a):
    beg = 0
    end = len(a)-1
    while(beg < end):
        if a[beg] != a[end]:
            return False
        beg += 1
        end -= 1 

    return True

print(is_palindrome_two('deeeed'))