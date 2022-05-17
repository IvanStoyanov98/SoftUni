my_list = input().split(" ")
float_list = list(map(float, my_list))
rounded_list = [round(x) for x in float_list]
print(rounded_list)