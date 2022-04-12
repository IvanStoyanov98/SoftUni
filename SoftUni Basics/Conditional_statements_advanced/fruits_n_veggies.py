something = input()

fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
veggies = ["tomato", "cucumber", "pepper", "carrot"]

if something in fruits:
    print("fruit")
elif something in veggies:
    print("vegetable")
else:
    print("unknown")