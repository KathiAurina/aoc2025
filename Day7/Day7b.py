
num_splits = 0
num_paths = 1

def input_to_matrix(filename, num_rows, num_cols):
    matrix = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            one_line = [] 
            for ch in line:
                if ch == "\n":
                    break
                one_line.append(ch)
            if len(one_line) != num_cols:
                print(f"line too short, len = {len(one_line)}")
                return [] 
            matrix.append(one_line)
        if len(matrix) != num_rows:
            print("input doesn't match shape of matrix")
            return []        
    return matrix

def change_row(matrix, row_index):
    global num_paths
    new_matrix = matrix.copy()
    prior_row = new_matrix[row_index - 1]
    current_row = new_matrix[row_index]
    
    for i, c in enumerate(current_row):
        if prior_row[i] == "|":
            if c == "^":
                current_row[i -1] = "|"
                current_row[i + 1] = "|"
                num_paths += 1
            elif c == ".":
                current_row[i] = "|" 
        
    return new_matrix

 
rows = 16 #142 #16
cols = 15 #141 #15
source = input_to_matrix("test_input.txt", rows, cols)

for i, c in enumerate(source[0]):
    if c == "S":
        source[1][i] = "|"

target = source.copy()



for i in range(2, rows):
    target = change_row(source, i)
    if target == []:
        print("error occured")
        break
    source = target


print(num_paths)
