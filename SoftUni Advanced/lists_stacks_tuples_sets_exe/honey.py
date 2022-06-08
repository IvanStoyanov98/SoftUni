from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(y) for y in input().split()]
operators = deque(input().split())

total_honey = 0

while bees and nectar and operators:

    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_operator = operators.popleft()
        honey = 0

        if current_operator == "+":
            honey = abs(current_bee + current_nectar)
        elif current_operator == "-":
            honey = abs(current_bee - current_nectar)
        elif current_operator == "*":
            honey = abs(current_bee * current_nectar)
        elif current_operator == "/":
            if current_nectar == 0:
                continue
            else:
                honey = abs(current_bee / current_nectar)

        total_honey += honey

    else:
        bees.appendleft(current_bee)
        continue

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")

