n = int(input())

my_set = set()

for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == "IN":
        my_set.add(car_number)
    elif direction == "OUT" and my_set:
        my_set.remove(car_number)

if my_set:
    for car in my_set:
        print(car)
else:
    print(f"Parking Lot is Empty")