from collections import deque
number_of_stations = int(input())

gas_stations = deque()


for _ in range(number_of_stations):
    gas_stations.append([int(x) for x in input().split()])

for attempt in range(number_of_stations):
    gud = True
    liters = 0

    for petrol, distance in gas_stations:
        liters += petrol - distance
        if liters < 0:
            gud = False
            break

    if not gud:
        gas_stations.append(gas_stations.popleft())
    else:
        print(attempt)
        break
