#Program to check if a string is a number

str1=input("Please enter first number: ")
str2=input("Please enter first number: ")

if str1.isdigit() and str2.isdigit():
    print("%s / %s = %0.2f"%(str1, str2, int(str1)/int(str2)))
else:
    print("NaN")
