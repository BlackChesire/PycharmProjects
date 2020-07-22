# Program to calculate the sum of digits in a 3 digits number

import random

#num = int(input("enter a 3 digits number: "))
#num = random.random() * 900 + 100
#num = random.uniform(100,1000)
#num = int(num)
num = random.randint(100,999)
x1 = num//100
x2 = (num//10)%10
x3 = num %10

print ("the sum of digits in {0} is: {1}".format(num, x1+x2+x3))