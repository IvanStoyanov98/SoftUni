number = int(input())
key_word = input()
my_list = list()
my_other_list = list()
for a in range(number):
    new_string = input()
    my_list.append(new_string)
    if key_word in new_string:
        my_other_list.append(new_string)

print(my_list)
print(my_other_list)