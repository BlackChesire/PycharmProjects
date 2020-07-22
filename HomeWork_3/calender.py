"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 3
Program: calender.py
"""
Name_Of_Month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November',
                 'December')
weekday = ('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')


def DaysCalc(year):  # calcs the days from the input "year" till 1990
    if leap(year) is False:
        dayclac = ((year - 1900) * 365.242) + 2
    else:
        dayclac = ((year - 1900) * 365) + 2
    return dayclac


def leap(year):  # checking if the year requested is leaped
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def firstdaycalibrate(year, month):  # syncing the first day of the month
    first_day = DaysCalc(year) + sumofdays(month, year)
    day1 = round(first_day) % 7
    return day1


def Monthleapsync(month, year):  # giving the number of days in the month depends if the year is leaped
    if month in ('September', 'April', 'June', 'November'):
        month = 30
        return month

    elif month in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
        month = 31
        return month

    elif month == 'February' and leap(year) is True:
        month = 29
        return month

    elif month == 'February' and leap(year) is False:
        month = 28
        return month


def sumofdays(month, year):  # counting the days from the start of the year
    sum = 0
    for i in range(0, Name_Of_Month.index(month)):
        sum += Monthleapsync(Name_Of_Month[i], year)
    return sum


def calender(day, year, month):  # Calender printer
    print(month, year)
    daysCount = day
    for i in weekday:
        print("{:<3}".format(i), end="")
    print()
    for j in range(1, day):
        print("{:<3}".format(""), end="")
    for j in range(1, Monthleapsync(month, year) + 1):
        print("{:<3d}".format(j), end="")
        if daysCount % 7 == 0:
            print()
        daysCount += 1


year = int(input("Please enter the year of the date:"))
month = input("Enter the full name of the year's month:")
month = month.capitalize()  # to avoid input error
first_day = firstdaycalibrate(year, month)
calender(first_day, year, month)
