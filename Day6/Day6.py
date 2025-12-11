

result = 0
with open("input.txt", "r") as file:
    lines = file.readlines()

    math_operators = lines[4].split()
    
    first = lines[0].split()
    second = lines[1].split()
    third = lines[2].split()
    fourth = lines[3].split()
    
    for i in range(len(math_operators)):
        if math_operators[i] == "+":
            result += int(first[i]) + int(second[i]) + int(third[i]) + int(fourth[i]) 

        elif math_operators[i] == "*":
            result += int(first[i]) * int(second[i]) * int(third[i]) * int(fourth[i]) 

        else:
            print("WARNING: something went wrong")


print(result)
 
        







