
def input_to_matrix(input_txt, rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    
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
    end_row = min(rows - 1, i + 1)
    end_col = min(cols - 1, j + 1)

    if matrix[i][j] == 1:
        neighbors = []
        for k in range(start_row, end_row + 1):
            for l in range(start_col, end_col + 1):
                neighbors.append(matrix[k][l])
        return neighbors #todo remember that matrix[i][j] is also 1 and included in neighbors
    else:
        return []

def get_neighbor_count(neighbors):
    count = sum(neighbors)
    return count - 1 #because matrix[i][j]=1 and is included in neighbors

NUM_ROWS = 136
NUM_COLS = 136
matrix = input_to_matrix("input.txt", NUM_ROWS, NUM_COLS)
accessible_scrolls = 0
for i in range(NUM_ROWS):
    for j in range(NUM_COLS):
        neighbors = find_neighbors(matrix, i, j, NUM_ROWS, NUM_COLS)
        if len(neighbors) > 0:
            count = get_neighbor_count(neighbors)
            if count < 4:
                accessible_scrolls += 1

print(accessible_scrolls)


