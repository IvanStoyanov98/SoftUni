first = ["Monday", "Tuesday", "Friday"]
second = ["Wednesday", "Thursday"]
third = ["Saturday", "Sunday"]

day = input()
price = 0

if day in first:
    price = 12
elif day in second:
    price = 14
elif day in third:
    price = 16

print(price)