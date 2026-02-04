







def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm
result = lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The least common multiple of {num1} and {num2} is: {result}")
