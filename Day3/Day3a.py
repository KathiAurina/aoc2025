
def find_largest_digit(line):
    largest = 0
    for digit in line:
        if digit == '\n':
            continue
        if int(digit) > largest:
            largest = int(digit)
    return largest

sum = 0
with open("input_day3.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        largest = find_largest_digit(line.strip()[:-1])
        for index, digit in enumerate(line):
            if digit == '\n':
                continue
            if int(digit) == largest:
                second_largest = find_largest_digit(line[index + 1:])
                number = int(str(largest) + str(second_largest))
                sum += number
                break

print(sum)






