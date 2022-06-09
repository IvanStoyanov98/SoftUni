rows, columns = [int(x) for x in input().split(", ")]

matrix = []
result = [0] * 4
for _ in range(rows):
    matrix.append(
        [int(y) for y in input().split(", ")]
    )

for ri in range(rows - 1):
    for ci in range(columns - 1):
        square = matrix[ri][ci] + matrix[ri][ci + 1] + \
                 matrix[ri + 1][ci] + matrix[ri + 1][ci + 1]
        if square > sum(result):
            result[0] = matrix[ri][ci]
            result[1] = matrix[ri][ci + 1]
            result[2] = matrix[ri + 1][ci]
            result[3] = matrix[ri + 1][ci + 1]

print(result[0], result[1])
print(result[2], result[3])
print(sum(result))