# Program that fills a list with random numbers

from random import randint

def fill_list(lst, size, min, max):
    for i in range(size):
        lst.append(randint(min, max))


minimum = int(input("Min: "))
maximum = int(input("Max: "))
n = int(input("Quantity: "))
a = []

fill_list(a, n, minimum, maximum)

print(a)

"""  RUN DEMO
Min: 11
Max: 29
Quantity: 5
[12, 14, 27, 18, 22]
"""
