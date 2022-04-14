tournaments = int(input())
points = int(input())
starting = points
wins = 0
for n in range(tournaments):
    result = input()

    if result == "W":
        points += 2000
        wins += 1
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720

print(f"Final points: {points}")
print(f"Average points: {(points - starting) / tournaments:.0f}")
print(f"{wins / tournaments * 100:.2f}%")