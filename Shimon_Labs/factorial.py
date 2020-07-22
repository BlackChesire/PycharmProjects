# Program to calculate the factorial for an input number

def factorial(n):
    fact = 1  
    for i in range(1,n+1): 
        fact = fact * i 
    return fact

n = input("Please enter a number: ")
print(n+"!=",factorial(int(n)))
    
"""   RUN DEMO
Please enter a number: 6
6!= 720
"""