"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 3
Program: stats.py
"""
numbers = input("Enter numbers")


def convert(numbers):  # converts string to list
    NumbersList = list(numbers.split(" "))
    return NumbersList


NumsList = convert(numbers)

for i in range(0, len(NumsList)):  # converting any cell in the list from string type to integers
    NumsList[i] = int(NumsList[i])


def average(NumsList):  # calculating average
    return sum(NumsList) / len(NumsList)


ListAVG = average(NumsList)


def highestNumber(NumsList):  # finds the highest number in the list
    highestNUM = max(NumsList)
    return highestNUM


ListMax = highestNumber(NumsList)


def highest_index(NumsList):  # detecting the location of the highest number in the list
    highest = NumsList.index(max(NumsList))
    return highest


list_highest_index = highest_index(NumsList)


def lowestnumber(NumsList):  # finds the lowest number in the list
    lowestNum = min(NumsList)
    return lowestNum


ListMin = lowestnumber(NumsList)


def lowest_index(NumsList):  # detecting the location of the lowest number in the list
    Lowest_index = NumsList.index(min(NumsList))
    return Lowest_index


ListMinIndex = lowest_index(NumsList)


def check_rising_series(NumsList):  # checking if the type of the series i rising
    for i in range(len(NumsList) - 1):
        if NumsList[i] > NumsList[i + 1]:
            return False
    return True


def check_descending_series(NumsList):  # checking if the type of the series i descending
    for i in range(len(NumsList) - 1):
        if NumsList[i] < NumsList[i + 1]:
            return False
    return True


def check_type_of_series(NumsList):  # checking if the type of the series is neither descending or rising by using the previous functions
    if check_rising_series(NumsList):
        return "Rising"
    elif check_descending_series(NumsList):
        return "descending"
    else:
        return "neither descending or rising"


SeriesType = check_type_of_series(NumsList)
print("the average of the numbers is ", ListAVG)
print("the highest number you entered is", ListMax, " in cell", list_highest_index)
print("the lowest number you entered is", ListMin, "in cell", ListMinIndex)
print("the type of the series is ", SeriesType)
