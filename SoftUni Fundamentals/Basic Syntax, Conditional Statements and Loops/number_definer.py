number = float(input())
value = ''
if number == 0:
    value = 'zero'
elif number > 0:
    if number < 1:
        value = 'small positive'
    elif number > 1000000:
        value = 'large positive'
    else:
        value = 'positive'
else:
    if abs(number) < 1:
        value = 'small negative'
    elif abs(number) > 1000000:
        value = 'large negative'
    else:
        value = 'negative'

print(value)