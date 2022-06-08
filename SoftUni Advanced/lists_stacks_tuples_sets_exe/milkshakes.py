from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(y) for y in input().split(", ")])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()
    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    if chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    if cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(cup_of_milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)}')
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f'Milk: {", ".join(str(y) for y in cups_of_milk)}')
else:
    print("Milk: empty")