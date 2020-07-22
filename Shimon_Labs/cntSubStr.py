# Program to count how many '@' in an input string
import sys

#while True:
#    str = input("Please enter a string ")
#    if str == 'quit':
#        sys.exit("Bye Bye")
#    print("There are %d '@' in the string!"%(str.count('@')))
    

while True:
    cnt=0
    str = input("Please enter a string ")
    if str == 'quit':
        sys.exit("Bye Bye")
    for i in str:
        if i=='@':
            cnt+=1
    print("There are %d '@' in the string!"%(cnt))