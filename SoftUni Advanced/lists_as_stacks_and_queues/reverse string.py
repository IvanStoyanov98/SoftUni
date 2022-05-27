string = input()
my_stack = []

for letter in string:
    my_stack.append(letter)

reverse_string = ""

while my_stack:
    reverse_string += my_stack.pop()

print(reverse_string)
