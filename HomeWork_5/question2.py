"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 5
Program: question number 2
"""


def divide_number(number, list_of_dividers=[]):
    if number < 0:  # in case user entered negative number
        return print("Error!")
    if (number == 1 or number == 0) and len(list_of_dividers) == 0:  # in case user entered "1" or "0"
        return print(number)
    if number == 1:
        list_of_dividers.reverse()
        return print(*list_of_dividers, sep="*")     # prints the number with *
    for i in range(2, number + 1):
        if number % i == 0:
            list_of_dividers.append(i)
            return divide_number(number // i)


number = input("Please enter a number:")
while number.isdigit() is False:     # int input validation
    number = input("wrong input, please enter a positive number or e for exit:")
    if number.lower() == 'e':
        break
else:
    divide_number(int(number))
