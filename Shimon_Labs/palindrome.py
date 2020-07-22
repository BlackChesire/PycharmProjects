# Program to check if an input string is a palindrome

str = input("Please enter a string: ")
str=str.lower()
i=0
j=len(str)-1
flag=True
while(i<j):
    if not str[i].isalpha():
        i+=1
        continue
    if not str[j].isalpha():
        j-=1
        continue
    if str[i]!=str[j]:
        flag=False
        break
    i+=1
    j-=1
    
print("This is %sa palindrome!"%("" if flag else "not "))
        