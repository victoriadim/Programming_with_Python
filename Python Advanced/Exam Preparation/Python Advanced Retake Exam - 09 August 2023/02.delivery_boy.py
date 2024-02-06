rows, cols = ([int(el) for el in input().split()])
matrix = []
starting_pos = []

for row in range(rows):
    matrix_row = [int(el) if el.isdigit() else el for el in input()]
    matrix.append(matrix_row)
    if 'B' in matrix_row:
        starting_pos = [row, matrix[row].index('B')]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

curr_pos = starting_pos
while True:
    command = input()
    current_row, current_col = curr_pos[0] + directions[command][0], curr_pos[1] + directions[command][1]

    if not (0 <= current_row < rows and 0 <= current_col < cols):
        matrix[starting_pos[0]][starting_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    el = matrix[current_row][current_col]

    if el == "*":
        continue

    curr_pos = [current_row, current_col]

    if el == "A":
        matrix[current_row][current_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif el == "P":
        matrix[current_row][current_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif el == "-":
        matrix[current_row][current_col] = "."
        continue

for row in matrix:
    print(f"{''.join(row)}")