# Program to print all even numbers in a list 

def printEven(lst):
	if len(lst) == 0:
		return
	if lst[0]%2 == 0:
		print(lst[0], end=" ")
	printEven(lst[1:])

def main():
    lst = [1,2,3,4,5,6,7,8]
    printEven(lst)
    
main()