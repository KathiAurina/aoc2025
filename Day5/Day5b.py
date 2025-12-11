#! usr/bin/env python3 
from tqdm import tqdm


included_ranges = []


def add_range(start, end):
    included_ranges.append([start, end])
    check_ranges_list()

def check_ranges_list():
    for i in range(len(included_ranges)):
        start = included_ranges[i][0]
        end = included_ranges[i][1]
        for j in range(len(included_ranges)):
            if i == j:
                continue
            compared_range = included_ranges[j]
            if (start < compared_range[0] and end < compared_range[0]) or start > compared_range[1]:
                continue
            else:
                included_ranges[j] = fit_new_range(start, end, compared_range)

            
def fit_new_range(start, end, new_range):
    new_start = new_range[0]
    new_end = new_range[1]
    fitted_range = [0, 0]
    
    if start > new_start and end < new_end:
        fitted_range = new_range

    elif start > new_start and end > new_end:
        fitted_range[0] = new_start
        fitted_range[1] = end

    elif start < new_start and end < new_end:
        fitted_range[0] = start
        fitted_range[1] = new_end

    else:
        fitted_range[0] = start
        fitted_range[1] = end

    if fitted_range == [0, 0]:
        print("WARNING: fitted_range maybe was not modified!")

    check_ranges_list()
    
    return fitted_range


with open("input_fresh.txt", "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        myrange = line.split("-");
        start = int(myrange[0])
        end = int(myrange[1])

        add_range(start, end)

print(included_ranges)        
num_fresh = 0    
for r in included_ranges:
    num_fresh += r[1] - r[0] + 1

print(num_fresh)
        
