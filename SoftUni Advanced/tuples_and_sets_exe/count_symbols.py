some_input = input()

my_dict = {}

for symbol in some_input:

    if symbol not in my_dict:
        my_dict[symbol] = 0

    my_dict[symbol] += 1

for key, value in sorted(my_dict.items()):
    print(f"{key}: {value} time/s")