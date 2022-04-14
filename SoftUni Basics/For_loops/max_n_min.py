import sys
numbers = int(input())
min_n = sys.maxsize
max_n = -sys.maxsize

for n in range(numbers):
    new_n = int(input())
    if new_n > max_n:
        max_n = new_n
    if new_n < min_n:
        min_n = new_n

if min_n != sys.maxsize and max_n != -sys.maxsize:
    print(f"Max number: {max_n}")
    print(f"Min number: {min_n}")
    