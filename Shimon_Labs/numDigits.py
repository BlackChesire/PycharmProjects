#Program to calculate the digit of an input number
num = int(input("Please enter a number"))

cnt=0
sumDigits = 0
mult = 1

while num > 0:
    digit = num % 10
    cnt += 1
    if digit % 2:
        mult *= digit
    else:
        sumDigits += digit
    num = num // 10

print("cntDigit=", cnt)
print("SumDigits=", sumDigits)
print("ProductDigit=", mult)

"""  RUN DEMO
Please enter a number1234
cntDigit= 4
SumDigits= 6
ProductDigit= 3
"""