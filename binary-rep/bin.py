def binary_rep(num):
    return bin(num)[2:]

# and bitwise returns 1 if both the bits are 1 else 0:
def bit_and(num1, num2):
    return num1 & num2

# or bitwise returns 1 if either the bits (or both) are 1 else 0
def bit_or(num1, num2):
    return num1 | num2

# returns a binaries compliment
def bit_not(num1):
    return ~num1

# returns 1 if strictly one or the other bits are 1 else 0
def bit_x_or(num1, num2):
    return num1 ^ num2

# bitwise shift left and fills the void with zero effectively multiplying the number by sum power of two
def shift_left(x):
    return x << 2

# bitwise shift right and fills the void with zero effectively dividing the number by sum power of two
def shift_right(x):
    return x >> 2

# should return 10010
print(binary_rep(bit_and(19, 18)))

# shoudl return 10011
print(binary_rep(bit_or(19, 18)))

# should return -19
print(bit_not(18))

# should return 1
print(binary_rep(bit_x_or(19, 18)))

# should return 20
print(shift_left(5))

# should return 5
print(shift_right(20))
