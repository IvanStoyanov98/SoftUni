command = input()
count = 0
list_of_commands = ["coding", "dog", "cat", "movie", "CODING", "DOG", "CAT", "MOVIE"]

while command != "END":
    info = command

    if info in list_of_commands:
        if info.isupper():
            count += 2
        else:
            count += 1

        if count > 5:
            print(f"You need extra sleep")
    command = input()

if count <= 5:
    print(f"{count}")