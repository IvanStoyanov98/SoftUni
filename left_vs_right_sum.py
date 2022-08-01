numbers = int(input())
left_side = 0
right_side = 0
for number in range(numbers * 2):
    new_num = int(input())

    if number < numbers:
        left_side += new_num
    else:
        right_side += new_num

if left_side == right_side:
    print(f"Yes, sum = {left_side}")
else:
    print(f"No, diff = {abs(left_side - right_side)}")
