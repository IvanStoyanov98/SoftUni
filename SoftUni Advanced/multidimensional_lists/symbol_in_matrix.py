rows_n_columns = int(input())

matrix = []
for _ in range(rows_n_columns):
    matrix.append([x for x in input()])

symbol = input()
is_found = False

for row in range(rows_n_columns):
    if is_found:
        break
    for s in range(rows_n_columns):

        if symbol == matrix[row][s]:
            is_found = True
            print(f"({row}, {s})")
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")