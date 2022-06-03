my_dict = dict()

my_input = [float(x) for x in input().split()]

for n in my_input:

    if n not in my_dict:
        my_dict[n] = 0
    my_dict[n] += 1

for key, value in my_dict.items():
    print(f"{key} - {value} times")