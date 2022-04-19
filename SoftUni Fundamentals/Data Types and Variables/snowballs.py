number_of_snowballs = int(input())

best_snowball = 0
best_balls_weight = 0
best_ball_time = 0
best_ball_quality = 0
for snowball in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = (snowball_weight / time_needed) ** quality
    if snowball_value > best_snowball:
        best_snowball = snowball_value
        best_balls_weight = snowball_weight
        best_ball_time = time_needed
        best_ball_quality = quality

print(f'{best_balls_weight} : {best_ball_time} = {best_snowball:.0f} ({best_ball_quality})')