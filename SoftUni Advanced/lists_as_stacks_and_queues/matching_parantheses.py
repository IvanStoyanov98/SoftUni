formula = input()

stack = []
count = 0
for symbol in range(len(formula)):
    opening_bracket = 0
    closing_bracket = 0
    if formula[symbol] == "(":
        stack.append(symbol)
        count += 1

        if count <= 0:
            break

    elif formula[symbol] == ")":
        count -= 1
        if count < 0:
            break
        opening_bracket = stack.pop()
        closing_bracket = symbol + 1

    if count >= 0 and formula[symbol] == ")":
        print(formula[opening_bracket:closing_bracket])