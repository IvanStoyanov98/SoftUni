years = float(input())
gender = input()
title = ''
if gender == "f":
    if 0 <= years <= 16:
        title = "Miss"
    else:
        title = "Ms."
elif gender == "m":
    if 0 <= years <= 16:
        title = "Master"
    else:
        title = "Mr."

print(title)