budget = float(input())
statists = int(input())
clothing_per_statist = float(input())

background = budget * 0.1

statists_x = statists * clothing_per_statist

if statists > 150:
    statists_x *= 0.9

total_costs = statists_x + background

if total_costs <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_costs:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_costs - budget:.2f} leva more.")