inputs = int(input())

total_space = 255
space_taken = 0
for _ in range(1, inputs + 1):
    liters_add = int(input())
    if space_taken + liters_add > total_space:
        print('Insufficient capacity!')
        space_taken -= liters_add
    space_taken += liters_add

print(space_taken)
