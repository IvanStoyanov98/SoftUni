command = input()
budget = 0


while command != "End":
    destination = command
    money_needed = float(input())

    while budget < money_needed:
        money = float(input())
        budget += money

    print(f"Going to {destination}!")
    command = input()
    budget = 0

