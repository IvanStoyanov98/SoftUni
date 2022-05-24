import re

phones_numbers = input()

regex = r"\+359([ -])2\1\d{3}\1\d{4}\b"

viable = re.finditer(regex, phones_numbers)

viable_list = []
for number in viable:
    viable_list.append(number.group())

print(", ".join(viable_list))