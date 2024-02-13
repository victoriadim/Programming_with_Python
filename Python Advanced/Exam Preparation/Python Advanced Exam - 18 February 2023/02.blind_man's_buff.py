rows, cols = ([int(el) for el in input().split()])
matrix = []
my_pos = []
touched_opponents = 0
moves_made = 0

for row in range(rows):
    matrix_row = input().split(" ")
    matrix.append(matrix_row)
    if 'B' in matrix[row]:
        my_pos = [row, matrix[row].index('B')]
        matrix[my_pos[0]][my_pos[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == "Finish":
        break

    current_row, current_col = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if not 0 <= current_row < rows and 0 <= current_col < cols:
        continue
    elif matrix[my_pos[0]][my_pos[1]] == "O":
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = "-"
        continue

    el = matrix[current_row][current_col]

    if el == "P":
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = "-"
        touched_opponents += 1
        moves_made += 1

        if touched_opponents == 3:
            break

    elif el == "-":
        my_pos = [current_row, current_col]
        moves_made += 1

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves_made}")