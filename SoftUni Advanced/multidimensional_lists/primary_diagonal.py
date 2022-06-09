n = int(input())

matrix = []
result = 0
for index in range(n):
    matrix.append(
        [int(x) for x in input().split()]
    )
    result += matrix[index][index]

print(result)