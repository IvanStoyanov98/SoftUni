groups = int(input())
total_ppl = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for n in range(groups):
    people = int(input())
    total_ppl += people

    if people <= 5:
        p1 += people
    elif people <= 12:
        p2 += people
    elif people <= 25:
        p3 += people
    elif people <= 40:
        p4 += people
    else:
        p5 += people

print(f"{p1 / total_ppl * 100:.2f}%")
print(f"{p2 / total_ppl * 100:.2f}%")
print(f"{p3 / total_ppl * 100:.2f}%")
print(f"{p4 / total_ppl * 100:.2f}%")
print(f"{p5 / total_ppl * 100:.2f}%")