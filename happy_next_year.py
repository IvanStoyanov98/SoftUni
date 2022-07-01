year = int(input())
storage = []
not_distinct = True

while not_distinct:
    year += 1
    stringed_year = str(year)

    for digit in stringed_year:
        if digit not in storage:
            storage.append(digit)

    x = "".join(storage)

    if stringed_year == x:
        not_distinct = False

    storage.clear()
    stringed_year = ""

print(year)