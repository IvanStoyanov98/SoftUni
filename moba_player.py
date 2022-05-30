command = input()
players_dict = {}
points_dict = {}
while command != "Season end":
    if "->" in command:
        info = command.split(" -> ")
        player = info[0]
        position = info[1]
        skill = int(info[2])

        if player not in players_dict:
            players_dict[player] = dict()

        if position not in players_dict[player]:
            players_dict[player][position] = skill

        else:
            if skill > players_dict[player][position]:
                players_dict[player][position] = skill

    elif 'vs' in command:
        info = command.split(" vs ")
        player_one = info[0]
        player_two = info[1]

        if player_one in players_dict and player_two in players_dict:
            for position_one, points_one in players_dict[player_one].items():
                for position_two, points_two in players_dict[player_two].items():
                    if position_one == position_two:
                        if points_one > points_two:
                            del players_dict[player_two][position_two]
                            break
                        elif points_one < points_two:
                            del players_dict[player_one][position_one]
                            break
    command = input()

for player, position in players_dict.items():
    for players, points in position.items():
        if player not in points_dict:
            points_dict[player] = points
        else:
            points_dict[player] += points

for player, points in dict(sorted(points_dict.items(), key=lambda x: (-x[1], x[0]))).items():
    print(f"{player}: {points} skill")
    for role, role_points in dict(sorted(players_dict[player].items(), key=lambda y: (-y[1], y[0]))).items():
        print(f"- {role} <::> {role_points}")
