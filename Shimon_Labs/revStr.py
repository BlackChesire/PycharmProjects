# Program to reverse an input string and print it 10 times to the screen

str = input("please enter a string: ")
revStr = str[-1::-1]
i=10
while(i):
    print(revStr)
    i-=1