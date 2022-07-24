activities_list = ["coding", "CODING", "dog", "DOG", "cat", "CAT", "movie", "MOVIE"]

command = input()
count = 1
coffee_cups = 0

while command != "END":
    event = command

    if event in activities_list:

        if event.isupper():
            coffee_cups += 2
        else:
            coffee_cups += 1

    command = input()
    count += 1

    if count > 5:
        break

if count <= 5:
    print(coffee_cups)
else:
    print("You need extra sleep")
