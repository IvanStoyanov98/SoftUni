cubic_meters = float(input())

total_price = cubic_meters * 7.61
discount = total_price * 0.18

print(f"The final price is: {total_price - discount} lv.")
print(f"The discount is: {discount}")