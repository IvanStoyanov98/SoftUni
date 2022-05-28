lines = int(input())
stack = []

for _ in range(lines):
    query = input()

    if query.startswith("1"):
        query = query.split(" ")
        number = int(query[1])
        stack.append(number)

    elif query.startswith("2") and stack:
        stack.pop()

    elif query.startswith("3") and stack:
        print(max(stack))

    elif query.startswith("4") and stack:
        print(min(stack))

rev_stack = []
while stack:
    rev_stack.append(str(stack.pop()))

print(f"{', '.join(rev_stack)}")