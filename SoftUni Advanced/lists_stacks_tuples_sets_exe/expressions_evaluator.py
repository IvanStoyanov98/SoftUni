from collections import deque


def operation(nums, operator):
    if operator == "*":
        while len(nums) >= 2:
            first = nums.popleft()
            result = first * nums.popleft()
            nums.appendleft(result)
    elif operator == "+":
        while len(nums) >= 2:
            first = nums.popleft()
            result = first + nums.popleft()
            nums.appendleft(result)
    elif operator == "-":
        while len(nums) >= 2:
            first = nums.popleft()
            result = first - nums.popleft()
            nums.appendleft(result)
    elif operator == "/":
        while len(nums) >= 2:
            first = nums.popleft()
            result = first // nums.popleft()
            nums.appendleft(result)


operators = ["*", "+", "-", "/"]
my_deque = deque([x for x in input().split()])
current_deque = deque()
for el in my_deque:
    if el not in operators:
        current_deque.append(int(el))
    else:
        operation(current_deque, el)


print(*current_deque)
