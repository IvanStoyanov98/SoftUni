budget = float(input())
season = input()

destination = ""
cost = 0

if season == "summer" or season == "winter":
    if budget <= 100:
        destination = "Bulgaria"
        if season == "summer":
            cost = budget * 0.3
        elif season == "winter":
            cost = budget * 0.7
    elif budget <= 1000:
        destination = "Balkans"
        if season == "summer":
            cost = budget * 0.4
        elif season == "winter":
            cost = budget * 0.8
    else:
        destination = "Europe"
        cost = budget * 0.9

print(f"Somewhere in {destination}")
if destination == "Europe":
    print(f"Hotel - {cost:.2f}")
else:
    if season == "summer":
        print(f"Camp - {cost:.2f}")
    else:
        print(f"Hotel - {cost:.2f}")

