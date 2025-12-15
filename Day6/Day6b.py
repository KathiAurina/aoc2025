LENGTH = 4
COL_NUM = 1000
result = 0

def product(lst):
    p = 1
    for i in lst:
        p *= int(i)
    return p

def my_sum(lst):
    p = 0
    for i in lst:
        p += int(i)
    return p

def find_idx_of_next_zero_col(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
        
    for j in range(cols):
        current_col = []
        for i in range(rows):
            current_col.append(int(matrix[i][j]))

        if sum(current_col) == 0:
            return j



def get_one_chunk(matrix):
    #matrix must consist of single integers
        
    rows = len(matrix)
    cols = len(matrix[0])

    # TODO add 1 more empty list for real input
    chunk = [[], [], [], []]
    rest = [[], [], [], []]

    zero_col_idx = find_idx_of_next_zero_col(matrix)
    
    for k in range(zero_col_idx):
        for l in range(rows):
            chunk[l].append(int(matrix[l][k]))
     
    for m in range(zero_col_idx + 1, cols):
        for n in range(rows):
            rest[n].append(int(matrix[n][m]))

    return chunk, rest

def list_to_nums(lst):
    nums = []
    #only LENGTH long numbers
    for h in range(0, len(lst), LENGTH):
        current_num = ""
    
        for p in range(h, LENGTH + h):
            current_digit = lst[p]
            if current_digit != 0:
                current_num += str(current_digit)
        nums.append(current_num)    

    return nums

def get_numbers_from_chunk(chunk):
    numbers = []
    rows = len(chunk)
    cols = len(chunk[0])

    for j in range(cols):
        for i in range(rows):
            numbers.append(chunk[i][j]) 

    numbers = list_to_nums(numbers)
    return numbers
    

with open("input.txt", "r") as file:
    lines = file.readlines()

    math_operators = lines[LENGTH].split()
    # LENGTH=3 for test and LENGTH=4 for real input
    print("math_operators length: ", len(math_operators)) 
    input_matrix = []
    
    for i in range(LENGTH):
        
        zeroed = lines[i].replace( " ", "0")
        zeroed = zeroed.strip("\n")
        
        input_matrix.append(list(zeroed))

rest = input_matrix
for h in range(COL_NUM):

    #last chunk
    if h == COL_NUM - 1:
        numbers = get_numbers_from_chunk(rest)

    else:
        chunk, rest = get_one_chunk(rest)
        print(chunk)
        numbers = get_numbers_from_chunk(chunk)
        
    if math_operators[h] == "+":
        new = int(my_sum(numbers))
        result += new

    elif math_operators[h] == "*":
        new = int(product(numbers))
        result += new
        
    else:
        print("WARNING: something went wrong")

    
    
print("final result: ", result)
