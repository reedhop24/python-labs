def reverse_built_in(string):
    arr = [char for char in string]
    arr.reverse()
    return ''.join(arr)


def reverse_built_in_two(string):
    return string[::-1]


def reverse_iterative(string):
    arr = [char for char in string]
    a = 0
    b = len(string)-1
    while a < len(string)/2:
        holder = arr[a]
        arr[a] = arr[b]
        arr[b] = holder
        a += 1
        b -= 1
    return ''.join(arr)

print(reverse_iterative('nirvana'))
print(reverse_built_in('nirvana'))
print(reverse_built_in_two('nirvana'))