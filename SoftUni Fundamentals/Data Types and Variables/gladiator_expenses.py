lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shields_count = 0

for loss in range(1, lost_fights + 1):
    if loss % 2 == 0:
        expenses += helmet_price
    if loss % 3 == 0:
        expenses += sword_price
    if loss % 6 == 0:
        expenses += shield_price
        broken_shields_count += 1
        if broken_shields_count % 2 == 0:
            expenses += armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')