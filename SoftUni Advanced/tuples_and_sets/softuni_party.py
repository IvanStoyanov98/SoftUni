n = int(input())

vip = set()
normal = set()

for _ in range(n):
    code = input()
    x = code[0]

    if x.isdigit():
        vip.add(code)
    else:
        normal.add(code)

while True:
    new_input = input()

    if new_input == "END":
        break
    else:
        if new_input in vip:
            vip.remove(new_input)
        elif new_input in normal:
            normal.remove(new_input)

print(len(vip) + len(normal))
for guest in sorted(vip):
    print(guest)
for guest in sorted(normal):
    print(guest)