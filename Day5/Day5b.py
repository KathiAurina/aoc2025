 
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
                

def remove_similar_ranges():
    for i, rg in enumerate(included_ranges):
        start = rg[0]
        end = rg[1]
        for j in range(i, len(included_ranges)):
            if i == j:
                continue
            elif included_ranges[j][0] == start and included_ranges[j][1] == end:
                included_ranges.remove(included_ranges[j])
                        
        
def fit_new_range(start, end):
    global included_ranges
    problematic_ranges = []
       
    for i in range(len(included_ranges)):
        start_incl = included_ranges[i][0]
        end_incl = included_ranges[i][1]
        
        if check_one_range(start, end, (start_incl, end_incl)):
            continue
    
        else:
            problematic_ranges.append((start_incl, end_incl))

    fitted_start = start
    fitted_end = end
   
    for rg in problematic_ranges:
        start_rg = rg[0]
        end_rg = rg[1]

        if fitted_start > start_rg:
            fitted_start = start_rg
            
        if fitted_end < end_rg:
            fitted_end = end_rg

        included_ranges.remove(rg)
        
    included_ranges.append((fitted_start, fitted_end))
            

with open("input_fresh.txt", "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        myrange = line.split("-");
        start = int(myrange[0])
        end = int(myrange[1])
        if check(start, end):
            included_ranges.append((start, end))
        else:
            fit_new_range(start, end)
            check_all_ranges()
            remove_similar_ranges()
            
#print(included_ranges)        
num_fresh = 0    
for r in included_ranges:
    num_fresh += r[1] - r[0] + 1

print(num_fresh)
        
