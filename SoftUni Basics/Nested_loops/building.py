floors = int(input())
rooms = int(input())

type = ""

for floor in range(floors, 0, -1):

    if floor == floors:
        type = "L"
    elif floor != floors and floor % 2 == 0:
        type = "O"
    elif floor != floors and floor % 2 != 0:
        type = "A"

    for r in range(rooms):
        print(f"{type}{floor}{r}", end=" ")

    print("")

