text = input()
command_text = input().split(":|:")

while command_text[0] != "Reveal":
    command = command_text[0]
    if command == "InsertSpace":
        index = int(command_text[1])
        text = text[:index] + " " + text[index:]
        print(text)

    elif command == "Reverse":
        substring = command_text[1]
        if substring in text:
            substring_reversed = substring[::-1]
            text = text.replace(substring, substring_reversed, 1)
            print(text)
        else:
            print("error")

    elif command == "ChangeAll":
        substring = command_text[1]
        replacement = command_text[2]
        if substring in text:
            text = text.replace(substring, replacement)
            print(text)
    command_text = input().split(":|:")

print(f"You have a new text message: {text}")