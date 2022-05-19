users_input = input().split(", ")
my_list = []

for number in users_input:
    my_list.append(int(number))

for x in my_list:
    if x == 0:
        my_list.remove(x)
        my_list.append(x)
print(my_list)