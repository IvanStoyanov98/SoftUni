actor = input()
points = float(input())
jury = int(input())

for n in range(jury):
    jury_name = input()
    jury_points = float(input())

    points += (jury_points * len(jury_name)) / 2

    if points >= 1250.5:
        break

if points >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5 - points:.1f} more!")
