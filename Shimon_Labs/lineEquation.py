# Program to find the equation of the line (y=kx+b) passing through two known points

print("A(x1; y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("B(x2; y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Equation:")
a = (y1 - y2) / (x1 - x2)
b = y2 - a * x2
print("\ty = %.2f*x + %.2f" % (a, b))

"""  RUN DEMO
A(x1; y1):
        x1 = -1
        y1 = 2
B(x2; y2):
        x2 = 1.5
        y2 = -0.25
Equation:
        y = -0.90*x + 1.10
"""