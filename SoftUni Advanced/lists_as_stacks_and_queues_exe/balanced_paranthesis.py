from collections import deque

the_input = input()

my_dict = {
    ")": "(",
    "]": "[",
    "}": "{"
}

left_side = deque()
balanced = True

for parentheses in the_input:
    if parentheses in my_dict.values():
        left_side.append(parentheses)

    elif not left_side:
        balanced = False

    elif parentheses in my_dict.keys():
        last = left_side[-1]
        if last == my_dict[parentheses]:
            left_side.pop()

        else:
            balanced = False

    if not balanced:
        break

if not balanced or left_side:
    print("NO")
else:
    print("YES")
