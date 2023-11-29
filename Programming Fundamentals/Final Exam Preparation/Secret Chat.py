"""
On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
•	"InsertSpace:|:{index}":
o	Inserts a single space at the given index. The given index will always be valid.
•	"Reverse:|:{substring}":
o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
o	If not, print "error".
o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
•	"ChangeAll:|:{substring}:|:{replacement}":
o	Changes all occurrences of the given substring with the replacement text.
Input / Constraints
•	On the first line, you will receive a string with a message.
•	On the following lines, you will be receiving commands, split by ":|:".
Output
•	After each set of instructions, print the resulting string.
•	After the "Reveal" command is received, print this message:
"You have a new text message: {message}"
"""

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