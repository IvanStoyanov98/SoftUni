def add_item(sety, item):
    for x in item:
        sety.add(x)


def remove_item(setx, itemx):
    for y in itemx:
        if y in setx:
            setx.remove(y)


first_set = set([int(x) for x in input().split()])
second_set = set([int(y) for y in input().split()])

n = int(input())

for _ in range(n):
    command = input().split()

    first = command[0]
    second = command[1]
    third = [int(x) for x in command[2:]]

    if first == "Add":

        if second == "First":
            add_item(first_set, third)

        elif second == "Second":
            add_item(second_set, third)

    elif first == "Remove":

        if second == "First":
            remove_item(first_set, third)

        elif second == "Second":
            remove_item(second_set, third)

    elif first == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
