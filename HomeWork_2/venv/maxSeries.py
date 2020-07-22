"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 2
Program: MaxSeries.py
"""
listofNum = []
an = int(input("Please enter a number"))
while an != 0:
    listofNum.append(an)
    an = int(input("Please enter a number"))
print("the highest number is:", max(listofNum) , "in cell" ,listofNum.index(max(listofNum)) + 1)
print("the lowest number is:" , min(listofNum) , "in cell" ,listofNum.index(min(listofNum)) + 1)
print("Average is :",  sum(listofNum) / len(listofNum))
