first_word = input()
second_word = input()

for letter in range(len(first_word)):
    if first_word[letter] != second_word[letter]:
        replacement = second_word[letter]
        new_word = first_word[:letter] + replacement + first_word[letter + 1:]
        first_word = new_word
        print(first_word)