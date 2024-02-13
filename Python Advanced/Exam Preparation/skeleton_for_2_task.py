# if there are different integers for rows and cols
rows, cols = ([int(el) for el in input().split()])
matrix = []
my_pos = []

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


# if there is only one integer
size = int(input())
# commands = input().split(", ") if the commands are on the same line
matrix = []
my_pos = []

for row in range(size):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if 'S' in matrix_row:
        my_pos = [row, matrix[row].index('S')]
        matrix[my_pos[0]][my_pos[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}



while True:
    command = input()
    current_row, current_col = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if not (0 <= current_row < rows and 0 <= current_col < cols):
        # print something and break or continue

    el = matrix[current_row][current_col] # for the symbols in the matrix

    if el == "...":
        ...
    elif el == "...":

    matrix[my_pos[0]][my_pos[1]] = "?" # ? represent the symbol for the change when you step on the el

# for row in matrix:
#     print(f"{''.join(row)}")  # if there is a need for printing the whole matrix with no separation