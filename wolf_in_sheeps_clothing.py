the_list = input().split(", ")
counter = 0
for i in range(len(the_list) - 1, - 1, - 1):
    if the_list[i] != 'wolf':
        counter += 1
    if the_list[i] == "wolf" and i == len(the_list) - 1:
        print("Please go away and stop eating my sheep")
    elif the_list[i] == 'wolf':
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
