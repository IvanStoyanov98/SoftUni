rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append(
        [int(x) for x in input().split()]
    )

column_sums = [0] * columns

for index in range(rows):
    for col in range(columns):
        column_sums[col] += matrix[index][col]

print(*column_sums, sep="\n")
