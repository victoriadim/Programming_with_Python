row, col = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float('-inf')
sub_matrix = []

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        under_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        total_sum = current_element + next_element + under_element + diagonal_element

        if max_sum < total_sum:
            max_sum = total_sum
            sub_matrix = [[current_element, next_element], [under_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)