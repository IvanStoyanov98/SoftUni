number_of_orders = int(input())

order_cost = 0
total_cost = 0

for que in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    order_cost = price_per_capsule * days * capsules_count
    total_cost += order_cost
    print(f'The price for the coffee is: ${order_cost:.2f}')
print(f'Total: ${total_cost:.2f}')