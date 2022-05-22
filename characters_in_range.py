start = input()
end = input()

my_list = list(chr(a) for a in range(ord(start) + 1, ord(end)))
print(" ".join(my_list))
