flowers_dict = \
    {
        "Roses": 5,
        "Dahlias": 3.8,
        "Tulips": 2.8,
        "Narcissus": 3,
        "Gladiolus": 2.5
    }

flowers = input()
quantity = int(input())
budget = int(input())

cost = flowers_dict[flowers] * quantity

if flowers == "Roses" and quantity > 80:
    cost *= 0.9
elif flowers == "Dahlias" and quantity > 90:
    cost *= 0.85
elif flowers == "Tulips" and quantity > 80:
    cost *= 0.85
elif flowers == "Narcissus" and quantity < 120:
    cost *= 1.15
elif flowers == "Gladiolus" and quantity < 80:
    cost *= 1.2

if budget >= cost:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {budget - cost:.2f} leva left.")
else:
    print(f"Not enough money, you need {cost - budget:.2f} leva more.")