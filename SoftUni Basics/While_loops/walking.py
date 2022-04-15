goal = 10000
steps = 0

while True:

    how_many = input()
    if how_many == "Going home":
        new_steps = int(input())
        steps += new_steps
        break
    steps += int(how_many)

    if steps >= goal:
        break

if steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{steps - goal} steps over the goal!")
else:
    print(f"{goal - steps} more steps to reach goal.")