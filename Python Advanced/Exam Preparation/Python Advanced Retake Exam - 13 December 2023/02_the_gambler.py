money = 100
steps = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}


def get_start_pos(m):
    for i, row in enumerate(m):
        if 'G' in row:
            for j, pos in enumerate(row):
                if pos == 'G':
                    return [i, j]


def get_next(m, s, cp):
    m[cp[0]][cp[1]] = '-'
    return [cp[0] + steps[s][0], cp[1] + steps[s][1]]


def get_value(m, cp):
    return m[cur_pos[0]][cp[1]]


def update_money(value, m):
    if value == 'P':
        m -= 200
    elif value == 'W':
        m += 100
    elif value == 'J':
        m += 100000
    return m


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

cur_pos = get_start_pos(matrix)
while True:
    step = input()
    if step == 'end':
        matrix[cur_pos[0]][cur_pos[1]] = 'G'
        print(f'End of the game. Total amount: {money}$')
        break

    cur_pos = get_next(matrix, step, cur_pos)

    if cur_pos[0] < 0 or cur_pos[1] < 0 or cur_pos[0] > len(matrix) or cur_pos[1] > len(matrix):
        money = 0
        print('Game over! You lost everything!')
        break

    pos_value = get_value(matrix, cur_pos)
    money = update_money(pos_value, money)

    if money <= 0:
        matrix[cur_pos[0]][cur_pos[1]] = 'G'
        print('Game over! You lost everything!')
        break
    elif pos_value == 'J':
        matrix[cur_pos[0]][cur_pos[1]] = 'G'
        print(f'You win the Jackpot!\nEnd of the game. Total amount: {money}$')
        break

if money > 0:
    for row in matrix:
        print(''.join(row))
