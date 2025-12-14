import numpy as np

result = 0



with open("input.txt", "r") as file:
    lines = file.readlines()

    math_operators = lines[3].split()
    # TODO 3 to 4 when real input 
    input_matrix = np.matrix((3, len(math_operators)))
    for i in range(3):
        lines[i].replace(" ", "0")
        for j in range(len(lines[i])):
            input_matrix[i][j] = int(lines[i][j])
        
print(input_matrix)
    
    #first = lines[0].split()
    #second = lines[1].split()
    #third = lines[2].split()
    #fourth = lines[3].split()
    
    #for i in range(len(math_operators)):
     #   if math_operators[i] == "+":
            
            
      #      result += int(first[i]) + int(second[i]) + int(third[i])# + int(fourth[i]) 
#
 #       elif math_operators[i] == "*":
  #          result += int(first[i]) * int(second[i]) * int(third[i])# * int(fourth[i]) 
#
 #       else:
  #          print("WARNING: something went wrong")


print(result)
 
        







