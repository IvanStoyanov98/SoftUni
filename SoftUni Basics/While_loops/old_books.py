search = input()
counter = 0
book = input()
is_found = False

while book != "No More Books":

    if book == search:
        is_found = True
        break
    else:
        counter += 1

    book = input()

if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {counter} books.")