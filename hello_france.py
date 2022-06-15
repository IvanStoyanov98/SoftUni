items = input().split("|")
budget = float(input())
new_items_list = []
profit = 0
to_print_list = []
for item in items:
    current_item = item.split("->")
    item_type = current_item[0]
    price = float(current_item[1])

    if budget >= price:

        if item_type == "Clothes" and price <= 50:
            budget -= price
            profit += price * 0.4
            new_item_price = price + (price * 0.4)
            new_items_list.append(new_item_price)
            to_print_list.append(f'{new_item_price:.2f}')

        elif item_type == "Shoes" and price <= 35:
            budget -= price
            profit += price * 0.4
            new_item_price = price + (price * 0.4)
            new_items_list.append(new_item_price)
            to_print_list.append(f'{new_item_price:.2f}')

        elif item_type == "Accessories" and price <= 20.50:
            budget -= price
            profit += price * 0.4
            new_item_price = price + (price * 0.4)
            new_items_list.append(new_item_price)
            to_print_list.append(f'{new_item_price:.2f}')

total_sum = budget + sum(new_items_list)

print(" ".join(to_print_list))
print(f"Profit: {profit:.2f}")

if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
