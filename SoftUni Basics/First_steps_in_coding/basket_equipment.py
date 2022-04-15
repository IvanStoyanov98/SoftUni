yearly_tax = int(input())

shoes = yearly_tax * 0.6
uniform = shoes * 0.8
ball = uniform * 0.25
accessories = ball * 0.2

final_price = shoes + uniform + ball + accessories + yearly_tax
print(final_price)