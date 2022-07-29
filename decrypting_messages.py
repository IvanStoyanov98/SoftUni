key = int(input())
number_of_letters = int(input())

random_string = ''

for letter in range(1, number_of_letters + 1):
    code_letter = input()
    letter_value = ord(code_letter)
    new_letter = chr(letter_value + key)
    random_string += new_letter
print(random_string)