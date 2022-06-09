rows = int(input())

matrix = []

for _ in range(rows):
    evens = [int(x) for x in input().split(", ")]
    matrix.append([x for x in evens if x % 2 == 0])

print(matrix)