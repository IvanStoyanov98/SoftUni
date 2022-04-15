money_needed = float(input())
current_money = float(input())

counter = 0
days_in_total = 0

while current_money < money_needed:
    q = input()
    money = float(input())

    if q == "save":
        current_money += money
        counter = 0
    elif q == "spend":
        counter += 1
        if current_money - money < 0:
            current_money = 0
        else:
            current_money -= money

    days_in_total += 1

    if counter == 5:
        break

if counter < 5:
    print(f"You saved the money for {days_in_total} days.")
else:
    print(f"You can't save the money.\n{days_in_total}")
