digits = list(map(int, input()))
digits.sort()
new = []
for digit in range(len(digits) - 1, -1, -1):
    new.append(str(digits[digit]))