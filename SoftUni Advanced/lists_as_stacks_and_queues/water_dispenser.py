from collections import deque

quantity = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break

    else:
        queue.append(command)

while True:
    command = input()

    if command == "End":
        break

    elif "refill" in command:
        command = command.split(" ")
        liters = int(command[1])
        quantity += liters

    else:
        liters = int(command)

        if liters <= quantity:
            print(f"{queue.popleft()} got water")
            quantity -= liters
        else:
            print(f"{queue.popleft()} must wait")

print(f"{quantity} liters left")