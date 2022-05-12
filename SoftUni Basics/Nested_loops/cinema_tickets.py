command = input()

standard = 0
student = 0
kids = 0
total = 0
while command != "Finish":
    movie_tickets = 0
    movie = command
    seats = int(input())

    for x in range(1, seats + 1):
        ticket = input()

        if ticket == "End":
            break
        else:
            if ticket == "student":
                student += 1
            elif ticket == "kid":
                kids += 1
            elif ticket == "standard":
                standard += 1

            total += 1
            movie_tickets += 1

    print(f"{movie} - {movie_tickets / seats * 100:.2f}% full.")

    command = input()

print(f"Total tickets: {total}")
print(f"{student /  total * 100:.2f}% student tickets.")
print(f"{standard /  total * 100:.2f}% standard tickets.")
print(f"{kids /  total * 100:.2f}% kids tickets.")