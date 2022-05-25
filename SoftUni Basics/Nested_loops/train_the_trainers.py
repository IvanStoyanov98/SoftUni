jury = int(input())

total = 0
grades_num = 0

while True:
    new_input = input()
    current = 0
    current_sum = 0
    if new_input == "Finish":
        break
    else:
        for _ in range(jury):
            grade = float(input())
            total += grade
            grades_num += 1
            current += grade
            current_sum += 1

    print(f"{new_input} - {current / current_sum:.2f}.")

print(f"Student's final assessment is {total / grades_num:.2f}.")