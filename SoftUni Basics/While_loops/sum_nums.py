the_num = 0
sum = 0

while True:
    new_num = int(input())

    if the_num == 0:
        the_num = new_num
    else:
        sum += new_num

    if sum >= the_num:
        break

print(sum)
