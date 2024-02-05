def get_start_pos(matrix):
    for i, rows in enumerate(matrix):
        if 'G' in row:
            for j, pos in enumerate(row):
                if pos == 'G':
                    return [i, j]


def get_next_movement(command, matrix, curr_pos):
    row, col = curr_pos
    matrix[row][col] = '-'
    if command == "up":
        curr_pos[0] -= 1
    elif command == "down":
        curr_pos[0] += 1
    elif command == "left":
        curr_pos[1] -= 1
    elif command == "right":
        curr_pos[1] += 1


def get_value(matrix, curr_pos):
    return matrix[curr_pos[0]][curr_pos[1]]


def update_money(cur_char, money, if_jackpot):
    if cur_char == 'P':
        money -= 200
    elif cur_char == 'W':
        money += 100
    elif cur_char == 'J':
        if_jackpot = True
        money += 100000
    return money


size = int(input())
money = 100
matrix_size = []
jackpot = False

for _ in range(size):
    matrix_size.append(list(input()))

starting_position = get_start_pos(matrix_size)

for directions in range(size):
    if directions == 'end':
        matrix_size[starting_position[0]][starting_position[1]] = 'G'
        print(f'Finish game. Total amount: {money}')
        break
    cur_pos = get_next_movement(matrix_size, command, cur_pos)
    if cur_pos[0] < 0 or cur_pos[1] < 0 or cur_pos[0] > len(matrix_size) or cur_pos[1] > len(matrix_size):
        money = 0
        print('Game over! You lost everything!')
        break

    pos_value = get_value(matrix_size, cur_pos)
    money = update_money(pos_value, money)

    if money <= 0:
        matrix_size[cur_pos[0]][cur_pos[1]] = 'G'
        print('Game over! You lost everything!')
        break
    elif pos_value == 'J':
        matrix_size[cur_pos[0]][cur_pos[1]] = 'G'
        print('You win the Jackpot!')
        print(f'End of the game. Total amount: {money}')
        break
if money > 0:
    for row in matrix_size:
        print(''.join(row))