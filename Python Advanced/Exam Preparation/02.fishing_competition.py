def out_of_bounds(row:int, col:int, matrix_size: int):
    if row < 0:
        return matrix_size - 1, col
    elif row >= matrix_size:
        return 0, col
    elif col < 0:
        return row, matrix_size - 1
    elif col >= matrix_size:
        return row, 0

    return row, col


size = int(input())
matrix = []
my_row, my_col = 0, 0
fish_amount = 0
whirlpool = False

for current_row in range(size):
    matrix_row = [int(el) if el.isdigit() else el for el in input()]
    if 'S' in matrix_row:
        my_row, my_col = current_row, matrix_row.index('S')
    matrix.append(matrix_row)

matrix[my_row][my_col] = '-'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()
while command != "collect the nets":
    cur_row, cur_col = directions[command]

    my_row, my_col = out_of_bounds(cur_row + my_row, cur_col + my_col, size)
    if isinstance(matrix[my_row][my_col], int):
        fish_amount += matrix[my_row][my_col]
    elif matrix[my_row][my_col] == 'W':
        fish_amount = 0
        whirlpool = True

    matrix[my_row][my_col] = '-'

    if whirlpool:
        break

    command = input()

matrix[my_row][my_col] = 'S'

if whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{my_row},{my_col}]")
elif fish_amount >= 20:
    print("Success! You managed to reach the quota!")
elif fish_amount < 20:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_amount} tons of fish more.")

if fish_amount:
    print(f"Amount of fish caught: {fish_amount} tons.")

if not whirlpool:
    [print(*row, sep="") for row in matrix]