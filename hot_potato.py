from collections import deque

kids_list = input().split(" ")
kids = deque(kids_list)

toss = int(input())

while len(kids) > 1:
    counter = 1

    while counter < toss:
        current_kid = kids.popleft()
        kids.append(current_kid)
        counter += 1
    else:
        print(f"Removed {kids.popleft()}")
        counter = 0

print(f"Last is {kids.pop()}")