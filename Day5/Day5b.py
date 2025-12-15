 
from tqdm import tqdm


included_ranges = []

def check(start, end):
    global included_ranges
    
    for i in range(len(included_ranges)):
        start_incl = included_ranges[i][0]
        end_incl = included_ranges[i][1]

        if not ((start_incl < start and end_incl < start) or start_incl > end):
                return False

    return True


def check_one_range(start, end, range_to_be_checked_against):
    start_r = range_to_be_checked_against[0]
    end_r = range_to_be_checked_against[1]
        
    if not ((start_r < start and end_r < start) or start_r > end):
        return False

    return True
        
def check_all_ranges():
    global included_ranges

    for i in range(len(included_ranges) - 1):
        first_range = included_ranges[i]
        for j in range(i, len(included_ranges)):
            second_range = included_ranges[i + 1]
            if check_one_range(first_range[0], first_range[1], second_range):
                continue
            else:
                # TODO hier noch endlosschleife verhindern
                fit_new_range(first_range[0], first_range[1])            
                

                        
        
def fit_new_range(start, end):
    global included_ranges
    
    for i in range(len(included_ranges)):
        start_incl = included_ranges[i][0]
        end_incl = included_ranges[i][1]
        
        if check_one_range(start, end, (start_incl, end_incl)):
            continue
        
        else:
            print("finding problematic range")        
            if start > start_incl and end < end_incl:
                print("if")
                fitted_range = (start_incl, end_incl)

            elif start > start_incl and end > end_incl:
                print("elif1")
                fitted_range = (start_incl, end)

            elif start < start_incl and end < end_incl:
                print("elif2")
                fitted_range = (start, end_incl)

            else:
                print("else")
                fitted_range = (start, end)

            included_ranges[i] = fitted_range

            check_all_ranges()
            #remove_similar_ranges()
            

with open("test_input_fresh.txt", "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        myrange = line.split("-");
        start = int(myrange[0])
        end = int(myrange[1])
        if check(start, end):
            included_ranges.append((start, end))
        else:
            print(f"found unfitting range ({start}, {end})")
            fit_new_range(start, end)
            
print(included_ranges)        
num_fresh = 0    
for r in included_ranges:
    num_fresh += r[1] - r[0] + 1

print(num_fresh)
        
