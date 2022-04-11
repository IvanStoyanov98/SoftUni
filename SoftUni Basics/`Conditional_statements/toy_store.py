vacation = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
toy_trucks = int(input())

total_quantity = puzzles + dolls + teddy_bears + minions + toy_trucks
total_price = puzzles * 2.6 + dolls * 3 + teddy_bears * 4.1 + minions * 8.2 + toy_trucks * 2

if total_quantity >= 50:
    total_price *= 0.75

rent = total_price * 0.1

diff = total_price - rent

if diff >= vacation:
    print(f"Yes! {diff - vacation:.2f} lv left.")
else:
    print(f"Not enough money! {vacation - diff:.2f} lv needed.")