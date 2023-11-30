"""
tired of it that you decided to help yourself with an intelligent solution.
Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:
•	"TakeOdd"
o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
•	"Cut {index} {length}"
o	Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
o	The given index and the length will always be valid.
•	"Substitute {substring} {substitute}"
o	If the raw password contains the given substring, replace all of its occurrences with the substitute text given and print the result.
o	If it doesn't, prints "Nothing to replace!".
Input
•	You will be receiving strings until the "Done" command is given.
Output
•	After the "Done" command is received, print:
o	"Your password is: {password}"
Constraints
•	The indexes from the "Cut {index} {length}" command will always be valid.
"""

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