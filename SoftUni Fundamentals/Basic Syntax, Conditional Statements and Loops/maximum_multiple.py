divider = int(input())
ceiling = int(input())
max_number = 0

for number in range(ceiling, divider + 1, -1):
    if number % divider == 0:
        max_number = number
        break
print(max_number)

# divider = int(input())
# ceiling = int(input())
# max_number = 0
#
# for number in range(divider + 1, ceiling + 1):
#     if number % divider == 0:
#         max_number = number
# print(max_number)
