message = input()
command = input()

while command != "Decode":
    info = command.split("|")
    type = info[0]

    if type == "Move":
        number_of_letters = int(info[1])

        first_half = message[:number_of_letters]
        second_half = message[number_of_letters::]
        message = second_half + first_half

    elif type == "Insert":
        index = int(info[1])
        value = info[2]

        first_half = message[:index]
        second_half = message[index::]
        message = first_half + value + second_half

    elif type == "ChangeAll":
        substring = info[1]
        replacement = info[2]

        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")