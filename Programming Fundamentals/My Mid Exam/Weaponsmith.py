"""
You will receive parts of a name of a weapon - a line with string particles, separated by "|".
The particles will be in mixed order, and your task is to align them through given commands. You will be receiving them on separate lines until you are given the command "Done". The supported commands are:
•	"Add {particle} {index}":
o	You should add the particle at the given index if the index is valid.
•	"Remove {index}":
o	You should remove the particle at the given index if the index is valid.
•	"Check Even":
o	Print the elements at even index positions, separated by a single space.
•	"Check Odd":
o	Print the elements at odd index positions, separated by a single space.
An index is valid when it is between 0 and the index of the last element inclusive.
When you receive "Done", the weapon name is considered correct, and you should print the particles in their current order joined together in the following format: "You crafted {weaponName}!".
Input
•	On the first line, you will receive parts of the given weapon name in a mixed order separated by "|".
•	On the following lines, until the "Done" command, you will be receiving commands in the format described above.
"""
weapons = input().split("|")
commands = input().split()

while commands[0] != "Done":
    if commands[0] == "Add":
        particle = commands[1]
        index = int(commands[2])
        if 0 <= index < len(weapons):
            weapons.insert(index, particle)

    elif commands[0] == "Remove":
        index = int(commands[1])
        if 0 <= index < len(weapons):
            weapons.pop(index)

    elif commands[0] == "Check":
        if commands[1] == "Odd":
            for i in range(1, len(weapons), 2):
                print(weapons[i], end=" ")
        elif commands[1] == "Even":
            for i in range(0, len(weapons), 2):
                print(weapons[i], end=" ")
    commands = input().split()

print(f'\nYou crafted {"".join(weapons)}!')