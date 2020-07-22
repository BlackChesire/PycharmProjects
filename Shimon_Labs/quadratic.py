# Program to solve a quadratic equation of 3 input parameters

import math
def quadratic_solution(a,b,c):
    disc=b*b-4*a*c
    if disc < 0:
        return None
    if disc == 0:
        return -b/2/a
    return (-b-math.sqrt(disc))/2/a, (-b+math.sqrt(disc))/2/a

def get_numbers(s):
    numbers_list=[]
    numbers_list_str = s.split()
    for num in numbers_list_str:
        numbers_list.append(float(num))
    return numbers_list

parameters_string=input('Enter parameters for quadratic equation(a b c): ')
parameters=get_numbers(parameters_string)
solution = quadratic_solution(parameters[0], parameters[1], parameters[2])
if solution == None:
    print('No solution')
else:
    print(solution)
