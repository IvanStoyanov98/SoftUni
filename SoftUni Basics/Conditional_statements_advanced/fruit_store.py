week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruits_list = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
fruits = {}

fruit = input()
day = input()
quantity = float(input())

if day in week:
    if fruit in fruits_list:
        fruits = {"banana": 2.5,
                  "apple": 1.2,
                  "orange": 0.85,
                  "grapefruit": 1.45,
                  "kiwi": 2.7,
                  "pineapple": 5.5,
                  "grapes": 3.85}
        print(f"{fruits[fruit] * quantity:.2f}")
    else:
        print("error")

elif day in weekend:
    if fruit in fruits_list:
        fruits = {"banana": 2.7,
                  "apple": 1.25,
                  "orange": 0.9,
                  "grapefruit": 1.6,
                  "kiwi": 3,
                  "pineapple": 5.6,
                  "grapes": 4.2}
        print(f"{fruits[fruit] * quantity:.2f}")
    else:
        print("error")

else:
    print(f"error")

