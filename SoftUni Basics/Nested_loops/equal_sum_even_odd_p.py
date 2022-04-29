enter_number_one = int(input())
enter_number_two = int(input())

for number in range(enter_number_one, enter_number_two + 1):
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str(number)):
        if (index + 1) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")
