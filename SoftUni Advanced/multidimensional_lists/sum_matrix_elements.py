rows, columns = [int(x) for x in input().split(", ")]

matrix = []
result = 0
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    result += sum(row)

print(result)
print(matrix)