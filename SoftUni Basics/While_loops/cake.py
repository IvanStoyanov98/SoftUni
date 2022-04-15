a = int(input())
b = int(input()) * a

command = input()

while command != "STOP":
    b -= int(command)

    if b <= 0:
        break

    command = input()

if b <= 0:
    print(f"No more cake left! You need {abs(b)} pieces more.")
else:
    print(f"{b} pieces are left.")