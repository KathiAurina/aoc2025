import numpy as np
NUM_DIGITS_TEST = 15
NUM_DIGITS = 100

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
        num_free_spaces = 12
        activated_digits = ""

        from_idx = 0
        to_idx = NUM_DIGITS - num_free_spaces + 1

        for idx, digit in enumerate(line):
            if num_free_spaces == 0 or digit == '\n':
                break
            next_digit = find_largest_digit(line.strip()[from_idx:to_idx])
            if int(digit) != int(next_digit):
                from_idx += 1
                continue
            activated_digits += str(next_digit)
            num_free_spaces -= 1
            to_idx += 1
            from_idx += 1

        sum += int(activated_digits)

print(sum)






