word = input()
reverse = ''
for letter in range(len(word) - 1, -1, -1):
    reverse += word[letter]
print(reverse)