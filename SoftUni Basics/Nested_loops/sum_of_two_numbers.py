start = int(input())
end = int(input())
magic_num = int(input())

combination = 0
found = False

for i in range(start, end + 1):
    for y in range(start, end + 1):
        combination += 1
        if i + y == magic_num:
            found = True
            print(f"Combination N:{combination}")
            print(f"({i} + {y} = {magic_num})")
            break
    if found:
        break

if not found:
    print(f"{combination} combinations - neither equals {magic_num}")
