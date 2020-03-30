def multiply_without(a, b):
    res = 0

    while b > 0:
        if b & 1:
            res = res + a

        a = a << 1
        b = b >> 1

    return res

print(multiply_without(12, 6))