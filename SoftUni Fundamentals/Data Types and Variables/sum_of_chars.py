number_of_letter = int(input())

total_sum = 0

for letter in range(1, number_of_letter + 1):
    new_letter = input()
    new_letter_sum = ord(new_letter)
    total_sum += new_letter_sum
print(f"The sum equals: {total_sum}")