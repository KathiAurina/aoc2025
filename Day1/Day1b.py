

position = 50
zero_count = 0


#open file and read lines
with open("input_day1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        zero_passings = int(line[1:]) // 100
        zero_passing_once = 0
        steps = int(line[1:]) % 100
        if line.startswith("L"):
            if position - steps < 0:
                start_position = position
                rest = steps - position
                position = 100 - rest
                if start_position != 0 and position != 0:
                    zero_passing_once += 1
            else:
                position -= steps
        elif line.startswith("R"):
            if position + steps > 99:
                start_position = position
                rest = (position + steps) - 100
                position = rest
                if start_position != 0 and position != 0:
                    zero_passing_once += 1
            else:
                position += steps
        if position == 0:
            zero_count += 1
        zero_count += zero_passings + zero_passing_once
print("zero count:", zero_count)

