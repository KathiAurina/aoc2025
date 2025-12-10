import numpy as np


def input_to_matrix(input_txt, rows, cols):
    matrix = np.zeros((rows, cols))
    with open(input_txt, "r") as file:
        lines = file.readlines()
        current_line_idx = 0
        for line in lines:
            for i in range(len(line.strip())):
                if line[i] == '@':
                   matrix[current_line_idx][i] = 1
            current_line_idx += 1

    return matrix

def find_neighbors(matrix, i, j, rows, cols):

    start_row = max(0, i - 1)
    start_col = max(0, j - 1)
    end_row = min(rows, i + 2)
    end_col = min(cols, j + 2)

    if matrix[i][j] == 1:
        neighbors = []
        for k in range(start_row, end_row):
            for l in range(start_col, end_col):
                neighbors.append(matrix[k][l])
        return neighbors #todo remember that matrix[i][j] is also 1 and included in neighbors
    else:
        return []

def get_neighbor_count(neighbors):
    count = np.sum(neighbors)
    return count - 1 #because matrix[i][j]=1 and is included in neighbors

NUM_ROWS = 136
NUM_COLS = 136
matrix = input_to_matrix("input.txt", NUM_ROWS, NUM_COLS)
accessible_scrolls = 0
for i in range(10):
    for j in range(10):
        neighbors = find_neighbors(matrix, i, j, NUM_ROWS, NUM_COLS)
        if len(neighbors) > 0:
            count = get_neighbor_count(neighbors)
            if count < 4:
                accessible_scrolls += 1

print(accessible_scrolls)


