"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 2
Program:rectangle.py
"""
from datetime import datetime

start_time = datetime.now()

Length = int(input("Please enter the length of rectangle:"))
Character = input("Please enter a character:")
print(Length * Character)
print(Character, " " * (Length - 4), Character)
print(Character, " " * (Length - 4), Character)
print(Length * Character)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
