users_number = int(input())


for magic_number in range(1111, 9999 + 1):

    is_special = True

    for digit in str(magic_number):
        if int(digit) == 0 or users_number % int(digit) != 0:
            is_special = False
            break
    if is_special:
        print(magic_number, end=" ")
