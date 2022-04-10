chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

menus_sum = chicken_menu * 10.35 + fish_menu * 12.4 + vegan_menu * 8.15
desert = menus_sum * 0.2

print(f"{menus_sum + desert + 2.5}")