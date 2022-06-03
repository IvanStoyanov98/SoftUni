n = int(input())

odd = set()
even = set()

for row in range(1, n + 1):
    name = input()
    name_value = sum([ord(x) for x in name]) // row

    if name_value % 2 == 0:
        even.add(name_value)
    else:
        odd.add(name_value)


even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(*result, sep=", ")


