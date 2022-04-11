hours = int(input())
minutes = int(input())
minutes += 15

if minutes + 15 >= 60:
    minutes = minutes % 60
    hours += 1
if hours <= 23:
    if minutes < 10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")
else:
    hours = 0
    if minutes < 10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")

# adds 15m