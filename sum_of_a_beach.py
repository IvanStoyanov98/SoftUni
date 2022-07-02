string = input().lower()
counter = 0

sand = string.count("sand")
water = string.count("water")
fish = string.count("fish")
sun = string.count("sun")
counter = counter + sand + water + fish + sun
print(counter)