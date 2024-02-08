rows, cols = ([int(el) for el in input().split(",")])
matrix = []
my_pos = []
my_row, my_col = 0, 0
cheese = 0

for row in range(rows):
    matrix_row = list(input())
    matrix.append(matrix_row)
    if 'M' in matrix_row:
        my_pos = [row, matrix[row].index('M')]
    cheese += matrix_row.count('C')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while cheese > 0:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    current_row, current_col = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if not (0 <= current_row < rows and 0 <= current_col < cols):
        print("No more cheese for tonight!")
        break
    if matrix[current_row][current_col] == "@":
        continue

    el = matrix[current_row][current_col]

    if el == "T":
        matrix[my_pos[0]][my_pos[1]] = '*'
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = 'M'
        print("Mouse is trapped!")
        break

    if el == "C":
        matrix[my_pos[0]][my_pos[1]] = '*'
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = 'M'
        cheese -= 1

    if el == "*":
        matrix[my_pos[0]][my_pos[1]] = '*'
        my_pos = [current_row, current_col]
        matrix[my_pos[0]][my_pos[1]] = 'M'
        continue

if cheese == 0:
    print("Happy mouse! All the cheese is eaten, good night!")
for row in matrix:
    print(f"{''.join(row)}")