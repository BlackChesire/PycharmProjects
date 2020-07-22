# Program to create a matrix of numbers

def createMat1(size):
    # Nested list naive
    matrix = [] 
      
    for i in range(size): 
          
        # Append an empty sublist inside the list 
        matrix.append([]) 
          
        for j in range(size): 
            matrix[i].append(j) 
    return matrix

def createMat2(size):
    # Nested list comprehension 
    matrix = [[j for j in range(x)] for i in range(x)] 
    return matrix

#checking program   
x = int(input("What is the size of the matrix? "))
print(createMat2(x)) 


"""   RUN DEMO
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
"""