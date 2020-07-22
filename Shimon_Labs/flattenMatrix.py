# Program to flatten a nested list

def flattenMat1(mat):
    # Nested List Naive
    flatten_matrix = [] 
  
    for sublist in matrix: 
        for val in sublist: 
            flatten_matrix.append(val) 
    return flatten_matrix
 
def flattenMat2(mat):
    # Nested List Comprehension 
    return [val for sublist in matrix for val in sublist]
    
    #checking program      
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
print(flattenMat2(matrix))   

 