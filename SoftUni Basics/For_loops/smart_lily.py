age = int(input())
dishwasher_cost = float(input())
price_per_toy = int(input())

saved_money = 0
toys = 0
received_money = 0

for n in range(1, age + 1):
    if n % 2 == 0:
        if n == 2:
            received_money = 10
            saved_money += received_money

        else:
            received_money += 10
            saved_money += received_money
        saved_money -= 1

    else:
        toys += 1

saved_money += toys * price_per_toy

if saved_money >= dishwasher_cost:
    print(f"Yes! {saved_money - dishwasher_cost:.2f}")
else:
    print(f"No! {dishwasher_cost - saved_money:.2f}")
