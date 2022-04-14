tabs = int(input())
salary = float(input())

for tab in range(tabs):
    the_tab = input()

    if the_tab == "Facebook":
        salary -= 150
    elif the_tab == "Instagram":
        salary -= 100
    elif the_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(f"{salary:.0f}")
