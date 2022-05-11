number = int(input())

even = list()
odd = list()
positive = list()
negative = list()

for _ in range(number):
    new_number = int(input())
    if new_number % 2 == 0:
        even.append(new_number)
    else:
        odd.append(new_number)
    if new_number >= 0:
        positive.append(new_number)
    else:
        negative.append(new_number)

command = input()
print(eval(command))
