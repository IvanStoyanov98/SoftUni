from math import ceil

series = input()
episode_duration = int(input())
break_duration = int(input())

time_needed = break_duration / 8 + break_duration / 4
time_left = break_duration - time_needed

if time_left >= episode_duration:
    print(f"You have enough time to watch {series} and left with {ceil(time_left - episode_duration):.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(episode_duration - time_left):.0f} more minutes.")