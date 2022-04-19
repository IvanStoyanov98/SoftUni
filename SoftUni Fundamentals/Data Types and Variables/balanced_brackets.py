range_of_whatever = int(input())

first_counter = 0
second_counter = 0
consecutive = 0
value = False

for symbol in range(range_of_whatever):
    new_symbol = input()
    if new_symbol == ')':
        second_counter += 1
        consecutive = 0
    if new_symbol == '(':
        first_counter += 1
        consecutive += 1
        if consecutive % 2 == 0 and consecutive > 1:
            value = True

if value:
    print('UNBALANCED')
elif first_counter == second_counter:
    print(f'BALANCED')
else:
    print('UNBALANCED')