from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split(" ")])

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order <= quantity:
        quantity -= orders.popleft()
    else:
        break

if orders:
    my_list = [str(x) for x in orders]
    print(f'Orders left: {" ".join(my_list)}')
else:
    print("Orders complete")