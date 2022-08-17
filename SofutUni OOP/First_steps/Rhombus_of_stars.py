def figure(a, b):
    spaces = a - b - 1
    stars = b + 1
    return " " * spaces + ("* " * stars).strip()


def rhombus(n):
    return [figure(n, x) for x in range(n)] + \
        [figure(n, x) for x in range(n - 2, -1, -1)]


def print_rhombus(n):
    [print(row) for row in rhombus(n)]


number = int(input())
print_rhombus(number)
