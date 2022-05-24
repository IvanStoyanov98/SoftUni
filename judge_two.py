command = input()
contest_dict = {}
users_points = {}

while command != "no more time":
    info = command.split(" -> ")
    username = info[0]
    contest = info[1]
    points = int(info[2])

    if contest not in contest_dict:
        contest_dict[contest] = {}
    if username not in contest_dict[contest]:
        contest_dict[contest][username] = points
    else:
        if points > contest_dict[contest][username]:
            contest_dict[contest][username] = points

    command = input()

for contest, user in contest_dict.items():
    for username, points in user.items():
        if username not in users_points:
            users_points[username] = points
        else:
            users_points[username] += points

for contest, users in contest_dict.items():
    number = 1
    print(f"{contest}: {len(users)} participants")
    for user, points in dict(sorted(contest_dict[contest].items(), key=lambda pts: (-pts[1], pts[0]))).items():
        print(f"{number}. {user} <::> {points}")
        number += 1

print(f"Individual standings:")

number = 1

for user, points in sorted(users_points.items(), key=lambda pts: (-pts[1], pts[0])):
    print(f"{number}. {user} -> {points}")
    number += 1
