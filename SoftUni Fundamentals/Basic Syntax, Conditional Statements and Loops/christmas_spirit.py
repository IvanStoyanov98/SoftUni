quantity = int(input())
days = int(input())

total_cost = 0
spirit = 0

for days_till_christmas in range(1, days + 1):

    if days_till_christmas % 11 == 0:
        quantity += 2

    if days_till_christmas % 2 == 0:
        ornament_set = 2 * quantity
        total_cost += ornament_set
        spirit += 5

    if days_till_christmas % 3 == 0:
        tree_skirts_garlands = 8 * quantity
        total_cost += tree_skirts_garlands
        spirit += 13

    if days_till_christmas % 5 == 0:
        tree_lights = 15 * quantity
        total_cost += tree_lights
        spirit += 17
        if days_till_christmas % 3 == 0:
            spirit += 30

    if days_till_christmas % 10 == 0:
        total_cost += 23    # 23 = tree_skirt_garlands and tree lights
        spirit -= 20
        if days_till_christmas == days:
            spirit -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')
