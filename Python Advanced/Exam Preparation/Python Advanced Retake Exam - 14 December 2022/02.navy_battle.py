size = int(input())
matrix = []
my_pos = []
damage = 0
battles = 0

for row in range(size):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if 'S' in matrix_row:
        my_pos = [row, matrix[row].index('S')]
        matrix[my_pos[0]][my_pos[1]] = "-"
    battles += matrix_row.count('C')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    current_row, current_col = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]
    my_pos = [current_row, current_col]
    el = matrix[current_row][current_col]

    if el == "-":
        continue

    elif el == "*":
        matrix[my_pos[0]][my_pos[1]] = '-'
        damage += 1
        if damage == 3:
            matrix[my_pos[0]][my_pos[1]] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{my_pos[0]}, {my_pos[1]}]!")
            break

    elif el == "C":
        matrix[my_pos[0]][my_pos[1]] = '-'
        battles -= 1
        if battles == 0:
            matrix[my_pos[0]][my_pos[1]] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

for row in matrix:
    print(f"{''.join(row)}")