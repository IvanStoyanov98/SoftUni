bad_grades = int(input())

counter = 0
all_tasks = 0
last_task = ""
average = 0

task = input()

while task != "Enough":
    all_tasks += 1
    last_task = task

    grade = float(input())
    average += grade

    if grade <= 4:
        counter += 1

    if counter >= bad_grades:
        break

    task = input()

if counter < bad_grades:
    print(f"Average score: {average / all_tasks:.2f}")
    print(f"Number of problems: {all_tasks}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {counter} poor grades.")