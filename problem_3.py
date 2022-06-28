heroes_dict = {}

command = input()

while command != "End":
    info = command.split(" ")
    type = info[0]

    if type == "Enroll":
        hero = info[1]

        if hero not in heroes_dict:
            heroes_dict[hero] = list()
        else:
            print(f"{hero} is already enrolled.")

    elif type == "Learn":
        hero = info[1]
        spell = info[2]

        if hero not in heroes_dict:
            print(f"{hero} doesn't exist.")
        else:
            if spell not in heroes_dict[hero]:
                heroes_dict[hero].append(spell)
            else:
                print(f"{hero} has already learnt {spell}")

    elif type == "Unlearn":
        hero = info[1]
        spell = info[2]

        if hero not in heroes_dict:
            print(f"{hero} doesn't exist.")
        else:
            if spell not in heroes_dict[hero]:
                print(f"{hero} doesn't know {spell}")
            else:
                heroes_dict[hero].remove(spell)

    command = input()

print("Heroes:")
for a_hero in heroes_dict:
    print(f"== {a_hero}: {', '.join(heroes_dict[a_hero])}")