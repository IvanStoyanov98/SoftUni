pens_quantity = int(input())
markers_quantity = int(input())
liters_cleaner = int(input())
discount = int(input()) / 100

total_cost = pens_quantity * 5.8 + markers_quantity * 7.2 + liters_cleaner * 1.2
final_cost = total_cost - total_cost * discount
print(final_cost)