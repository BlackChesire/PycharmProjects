# Program to find the bigest number of 3

x=int(input("Please enter first number: "))
y=int(input("Please enter second number: "))
z=int(input("Please enter third number: "))

"""
bigest = x

if bigest < y:
    bigest = y
if bigest < z:
    bigest = z
"""
   
if y <= x >= z:
    bigest = x
elif x <= y >= z:
    bigest = y
elif x <= z >= y:
   bigest = z
    
print("\nthe big4est number is:",bigest)
   

"""  RUN DEMO
Please enter first number: 8

Please enter second number: 2

Please enter third number: 4

the bigest number is: 8
"""