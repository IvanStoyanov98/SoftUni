from collections import deque

substrings = deque(input().split())

primary = {"red", "yellow", "blue"}
secondary = {"orange", "purple", "green"}
collected = []

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ""

    result = left + right
    if result in primary or result in secondary:
        collected.append(result)
        continue

    result = right + left
    if result in primary or result in secondary:
        collected.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        substrings.insert(len(substrings) // 2, left)
    if right:
        substrings.insert(len(substrings) // 2, right)

result = []

secondary_dict = {
    "orange": ['red', 'yellow'],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for color in collected:
    if color in primary:
        result.append(color)
        continue

    is_gud = True
    for base_color in secondary_dict[color]:
        if base_color not in collected:
            is_gud = False
            break

    if is_gud:
        result.append(color)

print(result)
