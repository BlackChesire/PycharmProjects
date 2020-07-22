# Program to find integers in an input string

str = input("Please enter a text: ")
l = len(str)

i=0
while i < l:
    num = ''
    symbol = str[i]
    while symbol.isdigit():
        num += symbol
        i+=1
        if i < l:
            symbol = str[i]
        else:
            break
    if num != '':
         print(num)
    i += 1
        
            