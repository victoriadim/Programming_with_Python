size = int(input())
matrix = []
my_pos = []
initial_armor = 300
enemies = 0

for row in range(size):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if 'J' in matrix_row:
        my_pos = [row, matrix[row].index('J')]
        matrix[my_pos[0]][my_pos[1]] = "-"
    enemies += matrix_row.count('E')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if initial_armor == 0:
        break

    current_row, current_col = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if matrix[current_row][current_col] == "-":
        matrix[my_pos[0]][my_pos[1]] = '-'
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = 'J'
        continue

    el = matrix[current_row][current_col]

    if el == "E":
        matrix[my_pos[0]][my_pos[1]] = '-'
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = 'J'
        enemies -= 1
        if enemies:
            initial_armor -= 100
            if initial_armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{my_pos[0]}, {my_pos[1]}]!")
                break
        elif enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

    elif el == "R":
        matrix[my_pos[0]][my_pos[1]] = '-'
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = 'J'
        initial_armor = 300

for row in matrix:
    print(*row, sep="")