numbers = input()
my_list = numbers.split(" ")
new_list = list()

for item in range(len(my_list)):
    new_item = int(my_list[item])
    if new_item > 0:
        new_item = -int(new_item)
    else:
        new_item = (abs(new_item))
    new_list.append(new_item)

print(new_list)

