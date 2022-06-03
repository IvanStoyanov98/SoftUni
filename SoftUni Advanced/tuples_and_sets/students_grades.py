n = int(input())

students_dict = {}

for _ in range(n):
    x = input().split()
    name = x[0]
    grade = float(x[1])

    if name not in students_dict:
        students_dict[name] = list()

    students_dict[name].append(grade)

for student, grades in students_dict.items():
    print(f"{student} ->", end=" ")
    for grade in grades:
        print(f"{grade:.2f}", end=" ")
    print(f"(avg: {sum(grades) / len(grades):.2f})")