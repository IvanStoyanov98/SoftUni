numbers = int(input())
positive = list()
negative = list()
for number in range(numbers):
    new_number = int(input())
    if new_number >= 0:
        positive.append(new_number)
    else:
        negative.append(new_number)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')