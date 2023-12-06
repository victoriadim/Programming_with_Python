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