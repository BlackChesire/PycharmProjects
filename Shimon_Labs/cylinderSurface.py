# Program to calculate The total surface area of the cylinder

# Import the constant pi from the math module.
from math import pi

# cylinder height
h = float(input("enter the cylinder's radius: "))

# cylinder base radius
r = float(input("enter the cylinder's height: "))

# A cylinder has two bases.
# Area of each is Pi * R * R.
circles = 2 * (pi * r**2)

# The area of the side surface of
# a cylinder is 2 * Pi * R * H.
side = 2 * pi * r * h

# total surface area
area = circles + side

print("the cylinder's surface area is: ", area)
