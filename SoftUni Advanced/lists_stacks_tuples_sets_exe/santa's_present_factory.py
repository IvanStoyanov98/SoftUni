from collections import deque
items_values = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

items_produced = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

is_done = False

materials = [int(x) for x in input().split()]
magic_levels = deque([int(y) for y in input().split()])

while materials and magic_levels:

    current_mat = materials.pop()
    current_magic = magic_levels.popleft()
    current_value = current_magic * current_mat

    for key, value in items_values.items():
        if value == current_value:
            items_produced[key] += 1
            break

    if current_mat == 0:
        if current_magic != 0:
            magic_levels.appendleft(current_magic)
        continue
    if current_magic == 0:
        if current_mat != 0:
            materials.append(current_mat)
        continue

    if current_value < 0:
        materials.append(current_mat + current_magic)
    elif current_value > 0 and current_value not in items_values.values():
        materials.append(current_mat + 15)


if items_produced["Doll"] > 0 and items_produced["Wooden train"] > 0:
    is_done = True
elif items_produced["Teddy bear"] > 0 and items_produced["Bicycle"] > 0:
    is_done = True

mats = [str(materials[x]) for x in range(len(materials) - 1, -1, -1)]
magi = [str(y) for y in magic_levels]

if is_done:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(mats)}")
if magic_levels:
    print(f"Magic left: {', '.join(magi)}")
for key, value in sorted(items_produced.items()):
    if items_produced[key] > 0:
        print(f"{key}: {value}")
