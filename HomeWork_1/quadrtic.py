"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 4
Program:digits.py
"""
"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 5
Program:quadratic.py
"""
import math

print("Please Enter a Quadratic type Equation")
a = float(input('Please enter a : '))
b = float(input('Please enter b : '))
c = float(input('Please enter c : '))
Undersqrt = (b ** 2) - (4 * a * c)
if a == b == c or Undersqrt < 0:
    print("no solution")
else:
    solution1 = (-b - math.sqrt(Undersqrt)) / (2 * a)
    solution2 = (-b + math.sqrt(Undersqrt)) / (2 * a)
    if solution2 == solution1:
        print("one solution", solution1)
    else:
        print("two solutions", solution1, solution2)
