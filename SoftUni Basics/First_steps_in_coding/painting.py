nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

total_sum = ((nylon + 2) * 1.5) + ((paint + paint * 0.1) * 14.5) + diluent * 5 + 0.4
workers_sum = (total_sum * 0.3) * hours

print(f"{total_sum + workers_sum}")