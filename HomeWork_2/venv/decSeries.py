"""
Student: Asaf Ben Shabat
ID: 312391774
Assignment no. 2
Program: decSeries.py
"""
list1 = []
count = 0
maxcount = 0
while len(list1) <  10:
    x = input("enter number")
    list1.append(x)
    for i in range(len(list1)):
        if list1[i] < list1[i-1]:
            count += 1
            if maxcount < count:
                maxcount = count
        if list1[i] >= list1[i-1]:
            count = 1

print("the lentgh of the longest series is:", maxcount)


