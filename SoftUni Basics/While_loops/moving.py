a = int(input())
b = int(input())
space = int(input()) * a * b

command = input()

while command != "Done":
    boxes = int(command)
    space -= boxes
    if space <= 0:
        break
    command = input()
if space <= 0:
    print(f"No more free space! You need {abs(space)} Cubic meters more.")
else:
    print(f"{space} Cubic meters left.")