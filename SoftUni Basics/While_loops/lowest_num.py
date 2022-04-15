import sys

lowest = sys.maxsize

command = input()

while command != "Stop":
    number = int(command)

    if number < lowest:
        lowest = number

    command = input()

print(lowest)
