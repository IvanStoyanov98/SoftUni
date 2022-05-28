clothes_stack = [int(x) for x in input().split(" ")]
rack_capacity = int(input())
capacity = rack_capacity
number_of_racks = 1

while clothes_stack:
    current_cloth = clothes_stack[-1]

    if current_cloth <= rack_capacity:
        rack_capacity -= clothes_stack.pop()
    else:
        number_of_racks += 1
        rack_capacity = capacity
        rack_capacity -= clothes_stack.pop()

print(number_of_racks)
