fire_cells = input().split('#')
water = int(input())
fire = 0
effort = 0
list_with_cells = []
for i in range(len(fire_cells)):
    split_cell = fire_cells[i].split(' ')
    value = int(split_cell[-1])
    if water >= value:
        if split_cell[0] == 'High':
            if 81 <= value <= 125:
                water -= value
                fire += value
                effort += value * 0.25
                list_with_cells.append(value)
            else:
                continue
        elif split_cell[0] == 'Medium':
            if 51 <= value <= 80:
                water -= value
                fire += value
                effort += value * 0.25
                list_with_cells.append(value)
            else:
                continue
        elif split_cell[0] == 'Low':
            if 1 <= value <= 50:
                water -= value
                fire += value
                effort += value * 0.25
                list_with_cells.append(value)
            else:
                continue
print('Cells:')
for i in range(len(list_with_cells)):
    print(f' - {list_with_cells[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire}')
