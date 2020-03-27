def fibonacci(num):
    num1 = 0
    num2 = 1
    count = 0
    while(count < num-1):
        temp = num2
        num2 = num1 + num2
        num1 = temp
        count += 1
    return num1

print(fibonacci(2))