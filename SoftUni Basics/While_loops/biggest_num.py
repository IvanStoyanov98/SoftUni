import sys

biggest = -sys.maxsize

command = input()

while command != "Stop":
    number = int(command)

    if number > biggest:
        biggest = number

    command = input()

print(biggest)
