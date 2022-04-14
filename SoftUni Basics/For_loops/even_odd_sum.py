numbers = int(input())
evens = 0
odds = 0

for n in range(numbers):
    new_num = int(input())

    if n % 2 == 0:
        evens += new_num
    else:
        odds += new_num

if evens == odds:
    print(f"Yes\nSum = {odds}")
else:
    print(f"No\nDiff = {abs(odds - evens)}")