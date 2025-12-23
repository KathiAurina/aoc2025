def init_matrix_with_zeros(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix        


def input_to_matrix(input_txt, rows, cols):

    matrix = init_matrix_with_zeros(rows, cols)
    
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


def remove_scrolls(matrix, removable_positions):

    new_matrix = matrix.copy()
    for pos in removable_positions:
        f = pos[0]
        g = pos[1]
        new_matrix[f][g] = 0

    return new_matrix

NUM_ROWS = 136
NUM_COLS = 136
matrix = input_to_matrix("input.txt", NUM_ROWS, NUM_COLS)

accessible_scrolls = 0
current_matrix = matrix
previous_matrix = init_matrix_with_zeros(NUM_ROWS, NUM_COLS)


def iterate():

    global current_matrix
    global previous_matrix
    global accessible_scrolls
    
    if current_matrix == previous_matrix:
        #print("current_matrix == previous_matrix -> return")
        return

    for i in range(NUM_ROWS):
         for j in range(NUM_COLS):
             previous_matrix[i][j] = current_matrix[i][j] 
   
    
        
    removable_positions = []
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            neighbors = find_neighbors(current_matrix, i, j, NUM_ROWS, NUM_COLS)
            if len(neighbors) > 0:
                count = get_neighbor_count(neighbors)
                if count < 4:
                    removable_positions.append((i, j))
                    accessible_scrolls += 1

    current_matrix = remove_scrolls(current_matrix, removable_positions)
    iterate()

iterate()
print(accessible_scrolls)


