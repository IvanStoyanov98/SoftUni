command = input()
total = 0

while command != "NoMoreMoney":
    money = float(command)

    if money >= 0:
        total += money
        print(f"Increase: {money}")
    else:
        print("Invalid Operation!")
    command = input()

print(f"Total: {total:.2f}")