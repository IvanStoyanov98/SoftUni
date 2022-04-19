first_number = int(input())
second_number = int(input())

invisible_variable = first_number
first_number = second_number

print('Before:')
print(f'a = {invisible_variable}')
print(f'b = {first_number}')
print('After:')
print(f'a = {first_number}')
print(f'b = {invisible_variable}')
