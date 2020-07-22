# Progam to put a space in an input string for each charcter other then a latin char

str = input("Please enter a string: ")
newStr=""
for i in str:
    if i.isalpha():
        newStr+=i
    else:
        newStr+=' '
        
print(newStr)