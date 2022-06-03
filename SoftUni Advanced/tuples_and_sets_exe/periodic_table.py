n = int(input())

periodic_table = set()

for _ in range(n):
    new_input = input()

    if " " in new_input:
        elements = [x for x in new_input.split()]
        while elements:
            periodic_table.add(elements.pop())
    else:
        periodic_table.add(new_input)

for el in periodic_table:
    print(el)