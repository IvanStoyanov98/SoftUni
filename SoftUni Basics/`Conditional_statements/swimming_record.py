import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

goal = distance_in_meters * time_per_meter
delay = math.floor(distance_in_meters / 15) * 12.5
total_time = goal + delay
difference = total_time - record_in_seconds

if total_time >= record_in_seconds:
    print(format(f"No, he failed! He was{difference: .2f} seconds slower."))

elif total_time < record_in_seconds:
    print(format(f"Yes, he succeeded! The new world record is{total_time: .2f} seconds."))