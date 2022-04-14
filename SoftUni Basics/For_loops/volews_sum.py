vowels = {"a": 1,
          "e": 2,
          "i": 3,
          "o": 4,
          "u": 5
          }

some_text = input()
value = 0

for symbol in some_text:
    if symbol in vowels:
        value += vowels[symbol]

print(value)