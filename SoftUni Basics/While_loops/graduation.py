student = input()

average_grade = 0
fails = 0
year = 1
count = 0

while fails <= 1 and year <= 12:
    grade = float(input())

    if grade >= 4:
        year += 1
        average_grade += grade
        count += 1

    else:
        fails += 1

if fails <= 1:
    print(f"{student} graduated. Average grade: {average_grade / count:.2f}")
else:
    print(f"{student} has been excluded at {year} grade")
