budget = float(input())
price_per_kg_flour = float(input())

eggs_price = price_per_kg_flour * 0.75
milk_price = price_per_kg_flour * 1.25  # equals 4 breads
milk_per_bread = milk_price / 4

price_for_one_bread = eggs_price + milk_per_bread + price_per_kg_flour
breads_count = 0
colored_eggs = 0

while price_for_one_bread <= budget:
    breads_count += 1
    colored_eggs += 3

    if breads_count % 3 == 0:
        colored_eggs -= breads_count - 2

    budget -= price_for_one_bread

print(f'You made {breads_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
