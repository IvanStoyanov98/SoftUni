n = int(input())

first_set = set()
second_set = set()
intersections_list = []

for _ in range(n):
    info = input().split("-")
    first = info[0]
    second = info[1]

    first_start, first_end = ([int(x) for x in first.split(",")])
    second_start, second_end = ([int(y) for y in second.split(",")])

    for num in range(first_start, first_end + 1):
        first_set.add(num)
    for num in range(second_start, second_end + 1):
        second_set.add(num)

    current_range = None

    if len(first_set.intersection(second_set)) >= len(second_set.intersection(first_set)):
        current_range = [x for x in first_set.intersection(second_set)]
    else:
        current_range = [y for y in second_set.intersection(first_set)]

    intersections_list.append(current_range)

    while first_set:
        first_set.pop()
    while second_set:
        second_set.pop()

longest = []

for item in intersections_list:
    if len(item) > len(longest):
        longest = item

print(f"Longest intersection is {longest} with length {len(longest)}")
