size = int(input())

matrix = []
my_pos = []
fish_amount = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    matrix_strings = [str(x) for x in row]

    if 'S' in matrix[row]:
        my_pos = [row, matrix[row].index('S')]
        matrix[row][my_pos[1]] = "*"

direction = input()
while direction != "collect the nets":

    row = my_pos[0] + directions[direction][0]
    col = my_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        if direction == "right":
            my_pos = [row, 0]
        elif direction == "left":
            my_pos = [row, size - 1]
        elif direction == "up":
            my_pos = [0, col]
        elif direction == "down":
            my_pos = [size - 1, col]

    my_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = "*"

    if element == "W":
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: {my_pos}")
        break

    if element.isdigit():
        fish_amount += int(element)
        matrix[row][col] = "-"

if fish_amount >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!\nYou need {20 - fish_amount} tons of fish more.")

if fish_amount > 0:
    print(f"Amount of fish caught: {fish_amount} tons.")

if 'W' not in matrix:
    print(matrix)