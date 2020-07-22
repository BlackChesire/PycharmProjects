# Program to delete a sub string from an input string

str = input("Please enter a string ")
subStr = input("What is the sub string to delete? ")
i = str.find(subStr)
while i>=0:
    before = str[:i-1]
    after = str[i+len(subStr):]
    str = before+after
    i = str.find(subStr)

print(str)