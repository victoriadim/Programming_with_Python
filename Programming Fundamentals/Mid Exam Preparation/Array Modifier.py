# values = [int(v) for v in input().split()]
# delimiter = "\n"
# end = "end"
# inn = input()
# commands = inn.split(delimiter)
#
# for command in commands:
#     if command == "end":
#         break
#     pos1 = int(command.split()[1])
#     pos2 = int(command.split()[2])
#     if command.split()[0] == "swap":
#         values[pos1], values[pos2] = values[pos2], values[pos1]
#     elif command.split()[0] == "multiply":
#         print("case_2")
#     elif command.split()[0] == "decrease":
#         print("case_2")
#
# print(values)


values = [int(v) for v in input().split()]
delimiter = " "
end = "end"
inn = input()
command = inn.split(delimiter)

while command[0] != end:
    if command[0] == "decrease":
        values = [v - 1 for v in values]
        command = input().split(delimiter)
        continue
    pos1 = int(command[1])
    pos2 = int(command[2])
    if command[0] == "swap":
        values[pos1], values[pos2] = values[pos2], values[pos1]
    elif command[0] == "multiply":
        values[pos1] = values[pos2] * values[pos1]

    command = input().split(delimiter)

print(str(values)[1: -1])