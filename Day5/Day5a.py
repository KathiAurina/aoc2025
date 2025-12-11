#! usr/bin/env python3 
from tqdm import tqdm
num_fresh = 0
available = set()
with open("input_available.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        available.add(int(line));

with open("input_fresh.txt", "r") as file:
    lines = file.readlines()
    for food_id in tqdm(available):
        for line in lines:
            myrange = line.split("-");
            start = int(myrange[0])
            end = int(myrange[1])

            if food_id < start or food_id > end:
                continue    
            else:
                num_fresh += 1
                break
                    

print(num_fresh)
        
