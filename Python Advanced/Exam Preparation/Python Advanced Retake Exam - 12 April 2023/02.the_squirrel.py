size = int(input())
commands = input().split(", ")
matrix = []
my_pos = []
hazelnuts = 0

for row in range(size):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if 's' in matrix_row:
        my_pos = [row, matrix[row].index('s')]
        matrix[my_pos[0]][my_pos[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for command in commands:
    my_pos[0] += directions[command][0]
    my_pos[1] += directions[command][1]

    if not (0 <= my_pos[0] < size and 0 <= my_pos[1] < size):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnuts}")
        break

    el = matrix[my_pos[0]][my_pos[1]]

    if el == "h":
        hazelnuts += 1
        if hazelnuts >= 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {hazelnuts}")
            break
    elif el == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts}")
        break

    matrix[my_pos[0]][my_pos[1]] = "*"

else:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts}")