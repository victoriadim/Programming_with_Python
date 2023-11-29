text = input()
commands_password = input().split()

while commands_password[0] != "Done":
    command = commands_password[0]
    if command == "TakeOdd":
        text = "".join([char for index, char in enumerate(text) if index % 2 != 0])
        print(text)

    elif command == "Cut":
        index = int(commands_password[1])
        length = int(commands_password[2])
        string = text[index:index + length]
        text = text.replace(string, "", 1)
        print(text)

    elif command == "Substitute":
        substring = commands_password[1]
        substitute = commands_password[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    commands_password = input().split()

print(f"Your password is: {text}")