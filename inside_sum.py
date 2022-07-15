import sys

numbers = int(input())

max_num = -sys.maxsize
total = 0

for n in range(numbers):
    new_num = int(input())
    total += new_num

    if new_num > max_num:
        max_num = new_num

total -= max_num

if max_num == total:
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(max_num - total)}")