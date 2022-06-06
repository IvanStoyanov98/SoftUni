list_with_people = input().split()
step = int(input())
index = 0
list_with_executed = []

while len(list_with_people) > 0:
    index += step - 1

    while index >= len(list_with_people):
        index -= len(list_with_people)

    list_with_executed.append(list_with_people[index])
    list_with_people.pop(index)

print(f"[{','.join(list_with_executed)}]")