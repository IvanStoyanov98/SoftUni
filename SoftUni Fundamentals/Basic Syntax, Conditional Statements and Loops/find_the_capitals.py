user_input = input()

my_list = []
upper_case_start = 65
upper_case_end = 91
for letter in range(len(user_input)):
    my_list.append(user_input[letter])
    print(my_list[letter])