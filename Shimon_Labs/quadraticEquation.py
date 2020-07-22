# Program to solve the quadratic equation

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b * b - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("x1 = %.2f; x2 = %.2f" % (x1, x2))
elif d == 0:
    x1 = -b / (2 * a)
    print("x1 = %.2f" % x1)
else:
    print("No roots")

"""  RUN DEMO
a = 4
b = -4
c = -5
x1 = 1.72; x2 = -0.72
"""
