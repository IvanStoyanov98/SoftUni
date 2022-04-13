operators = ["+", "-", "*", "/", "%"]
first = int(input())
second = int(input())
operator = input()

if operator in operators:

    if operator == "+":
        if first + second % 2 == 0:
            print(f"{first} {operator} {second} = {first + second} - even")
        else:
            print(f"{first} {operator} {second} = {first + second} - odd")

    elif operator == "-":
        if first - second % 2 == 0:
            print(f"{first} {operator} {second} = {first - second} - even")
        else:
            print(f"{first} {operator} {second} = {first - second} - odd")

    elif operator == "*":
        if first * second % 2 == 0:
            print(f"{first} {operator} {second} = {first * second} - even")
        else:
            print(f"{first} {operator} {second} = {first * second} - odd")

    elif operator == "/":
        if second != 0:
            print(f"{first} {operator} {second} = {first / second:.2f}")
        else:
            print(f"Cannot divide {first} by zero")

    else:   # num % num
        if second != 0:
            print(f"{first} {operator} {second} = {first % second}")
        else:
            print(f"Cannot divide {first} by zero")
