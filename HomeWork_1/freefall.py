"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 1
Program:freefall.py
"""
import math

g = float(9.8)
h = float(input("Please enter height"))
t = math.sqrt(2 * h / g)
v = g * t
print("it will take ", t, " seconds for the object to hit the ground")
print("the  falling speed of the object will be:", v)
