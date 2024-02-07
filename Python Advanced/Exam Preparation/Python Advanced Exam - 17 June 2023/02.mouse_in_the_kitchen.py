rows, cols = ([int(el) for el in input().split(",")])
matrix = []
starting_pos = []

for row in range(rows):
    matrix_row = [int(el) if el.isdigit() else el for el in input()]
    matrix.append(matrix_row)
    if 'M' in matrix_row:
        starting_pos = [row, matrix[row].index('M')]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
