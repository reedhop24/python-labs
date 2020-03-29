import math

def is_prime(x):
    if x == 2:
        return True
    elif x > 2 and x % 2 == 0:
        return False

    sqrt = math.floor(math.sqrt(x))

    for i in range(3, 1 + sqrt, 2):
        if x % i == 0:
            return False
    
    return x > 1

print(is_prime(9))