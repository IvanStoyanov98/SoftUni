number = int(input())

letter_one = 96
letter_two = 96
letter_three = 96
for first_letter in range(1, number + 1):
    letter_one += 1
    letter_two = 96
    letter_three = 96
    for second_letter in range(1, number + 1):
        letter_two += 1
        letter_three = 96
        for third_letter in range(1, number + 1):
            letter_three += 1
            print(f'{chr(letter_one)}{chr(letter_two)}{chr(letter_three)}')
