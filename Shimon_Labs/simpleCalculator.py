#Program to demonstrate a simple calculator

print("Zero as an operation sign "
      "will terminate the program")

while True:
    s = input("Sign (+,-,*,/): ")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Division by zero!")
    else:
        print("Invalid operation sign!")

"""  RUN DEMO
Zero as an operation sign will terminate the program
Sign (+,-,*,/): plus
Invalid operation sign!
Sign (+,-,*,/): +
x=5
y=-2.3
2.70
Sign (+,-,*,/): /
x=9
y=4
2.25
Sign (+,-,*,/): 0
"""