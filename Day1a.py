

position = 50
zero_count = 0


#open file and read lines
with open("input_day1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        steps = int(line[1:]) % 100
        if line.startswith("L"):
            if position - steps < 0:
                rest = steps - position
                position = 100 - rest
            else:
                position -= steps
        elif line.startswith("R"):
            if position + steps > 99:
                rest = (position + steps) - 100
                position = rest
            else:
                position += steps
        if position == 0:
            zero_count += 1
print("zero count:", zero_count)

