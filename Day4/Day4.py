

def count_at_chars(window):
    count = 0
    for c in window:
        if c == '@':
            count += 1
    return count

def find_num_for_line(line, half_window_size):
    num = 0
    line = line.strip('\n')
    for idx, ch in enumerate(line):
        if ch == '@':
            neighbors = 0
            if idx - half_window_size <= 0:
                neighbors += count_at_chars(line[0:idx])
            else:
                neighbors += count_at_chars(line[idx - half_window_size:idx])
            if idx + half_window_size >= len(line) - 1:
                neighbors += count_at_chars(line[idx + 1:])
            else:
                neighbors += count_at_chars(line[idx + 1:idx + half_window_size])

            if neighbors < 4:
                num += 1

    return num






sum_rolls = 0
with open("test_input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        sum_rolls += find_num_for_line(line, 4)

print(sum_rolls)

#TODO alles falsch, wir müssen auch die drüber und drunter beachten -> Matix bilden
