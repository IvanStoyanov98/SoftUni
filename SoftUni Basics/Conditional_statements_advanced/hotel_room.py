months = ["May", "June", "July", "August", "September", "October"]

month = input()
nights = int(input())

studio = 0
apartment = 0
if month in months:

    if month == "May" or month == "October":
        studio = 50
        apartment = 65
        if 7 < nights <= 14:
            studio *= 0.95
        elif 14 < nights:
            studio *= 0.7

    elif month == "June" or month == "September":
        studio = 75.2
        apartment = 68.7
        if 14 < nights:
            studio *= 0.8

    else:
        studio = 76
        apartment = 77

    if 14 < nights:
        apartment *= 0.9

print(f"Apartment: {apartment * nights:.2f} lv.")
print(f"Studio: {studio * nights:.2f} lv.")

