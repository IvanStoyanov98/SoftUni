lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (lenght * width * height) / 1000
needed_liters = volume * 0.83
print(needed_liters)