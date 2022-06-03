numbers_list = [int(x) for x in input().split()]
target_number = int(input())

iterator = 0
pairs_set = set()

for first_number in range(len(numbers_list)):

    for second_number in range(first_number, len(numbers_list)):

        if second_number != first_number:
            iterator += 1
            if numbers_list[first_number] + numbers_list[second_number] == target_number:
                print(f"{numbers_list[first_number]} + {numbers_list[second_number]} = {target_number}")
                pairs_set.add((numbers_list[first_number], numbers_list[second_number]))

print(f"Iterations done: {iterator}")
for pair in pairs_set:
    print(pair)