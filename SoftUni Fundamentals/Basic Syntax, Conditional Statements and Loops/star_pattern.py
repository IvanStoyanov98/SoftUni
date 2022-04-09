number = int(input())

for a in range(1, number + 1):
    for b in range(a):
        print('*', end='')
    print()
for a in range(number - 1, -1, -1):
    for b in range(a):
        print('*', end="")
    print()