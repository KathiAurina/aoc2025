import math
import sys



def initialize_square_matrix_with_zeros(length):
    matrix = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(0)
        matrix.append(row)
    return matrix


def get_coordinates():
    coordinates = []
    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        coords = line.strip().split(",")
        coordinates.append(coords)
    return coordinates


def calculate_distance(c1, c2):
    distance = 0
    distance += (int(c2[0]) - int(c1[0]))**2
    distance += (int(c2[1]) - int(c1[1]))**2
    distance += (int(c2[2]) - int(c1[2]))**2

    return math.sqrt(distance)

def get_two_closest_boxes(coordinates):
    shortest_distance = calculate_distance(coordinates[0], coordinates[1])
    pair = (coordinates[0], coordinates[1])
    for i in range(len(coordinates) - 1):
        for j in range(i, len(coordinates)):
            if i == j:
                continue
            new_dist = calculate_distance(coordinates[i], coordinates[j]) 
            if new_dist < shortest_distance: #TODO hier noch circuits prüfen
                shortest_distance = new_dist
                pair = (coordinates[i], coordinates[j])
    return pair
                
#box ist index der koordinaten in koordinaten liste
def add_box_to_circiuts(coordinates, box_idx, closest_box_idx, circuits):
    box = coordinates[box_idx]
    closest_box = coordinates[closest_box_idx]

    #both don't have circuit yet
    for circuit in circuits:
        if box not in circuit and closest_box not in circuit:
            continue




#hier fängt der Code an
NUM = 1000
my_coordinates = get_coordinates()
singles = []
circuits = []

for c in my_coordinates:
    singles.append(c)



###TODO smarter Ansatz wär einen Graphen zu modellieren und die 
###Kantengewichte sind die distances
###dann die 10 kürzesten distances finden?


##lass erstmal nur die NUM kürzesten distances raussuchen

def create_distance_matrix(coordinates):
    matrix = initialize_square_matrix_with_zeros(len(coordinates))
    
    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            if i == j:
                matrix[i][i] = 0
            matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])
            matrix[j][i] = matrix[i][j]
            
    return matrix


def find_min(distance_matrix):

    mymin = sys.maxsize
    mycol = 0
    myrow = 0

    for i in range(len(distance_matrix)):
        for j in range(i, len(distance_matrix[0])):
            if i == j:
                continue
            if distance_matrix[i][j] < mymin:
                mymin = distance_matrix[i][j]
                myrow = i
                mycol = j
    
    return mymin, myrow, mycol


def get_indices_of_NUM_shortest_distances(NUM, distance_matrix):

    working_matrix = distance_matrix.copy()
    indices = []
    mins = []

    
    for i in range(NUM):
        my_min, row, col = find_min(working_matrix)
        working_matrix[row][col] = sys.maxsize
        indices.append((row, col))
        mins.append(my_min)

    return indices, mins
            

def build_circuits(indices):

    circuits = []
    
    
    for ic in indices:
        if len(circuits) == 0:
            circuits.append([ic[0], ic[1]])
            continue 
        in_ct = False
        for ct in circuits:
            if ic[0] in ct and ic[1] in ct:
                in_ct = True
            elif ic[0] in ct:
                ct.append(ic[1])
                in_ct = True
            elif ic[1] in ct:
                ct.append(ic[0])
                in_ct = True
        if in_ct == False:
            circuits.append([ic[0], ic[1]])

    return circuits    

def remove_duplicate_circuites(circuites):
    
    unique_circuits = []
    for ct in circuites:
        if ct not in unique_circuits:
            unique_circuits.append(ct)

    return unique_circuits


def fuse_circuits(circuits, idx1, idx2):
    if idx1 == idx2:
        print("something went terribly wrong")

    new_circuits = circuits.copy()
    
    for c in circuits[idx1]:
        if c not in circuits[idx2]:
            new_circuits[idx2].append(c)
    for d in circuits[idx2]:
        if d not in circuits[idx1]:
            new_circuits[idx1].append(d)

    return new_circuits 

def circuits_kuerzen(circuits):

    gekuerzt = False
        
    for i in range(len(circuits)):
        ct = circuits[i]
        for j in range(len(circuits)):
            if i == j:
                continue
            for c in ct:
                if c in circuits[j]:
                    gekuerzt = True
                    new_circuits = fuse_circuits(circuits, i, j)

    if not gekuerzt:
        new_circuits = circuits

    #sort circuits ascending
    for c in new_circuits:
        c.sort()

    new_circuits = remove_duplicate_circuites(new_circuits)
    
    return new_circuits



        
    
    
my_matrix = create_distance_matrix(my_coordinates)
myindices, mymins = get_indices_of_NUM_shortest_distances(NUM, my_matrix)
#print("my_matrix: ", my_matrix)
#print(myindices, ", ", mymins)
my_circuits = build_circuits(myindices)
#print("circuits: ", my_circuits)

gekuerzte_ct = circuits_kuerzen(my_circuits)
#print("gekuerzte_ct: ", gekuerzte_ct)

#multiply 3 largest circuits
def sort_by_length(lst):
    return len(lst)
gekuerzte_ct.sort(key=sort_by_length, reverse=True)
#print("sortierte: ", gekuerzte_ct)

product = len(gekuerzte_ct[0]) * len(gekuerzte_ct[1]) * len(gekuerzte_ct[2])
print("product: ", product)
