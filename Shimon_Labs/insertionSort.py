# Program to implement recursive insertion sort 

def insertionSortRecursive(lst): 
    n=len(lst)
    if n<=1: 
        return
	
	# Sort first n-1 elements 
    insertionSortRecursive(lst[:-1]) 
	#Insert last element at its correct position in sorted list
    last = lst[-1] 
    j = n-2
	
	# Move elements of arr[0..i-1], that are 
	# greater than key, to one position ahead 
	# of their current position 
    while (j>=0 and lst[j]>last): 
        lst[j+1] = lst[j] 
        j-=1

    lst[j+1]=last 
	
# A utility function to print an array of size n 
def printArray(lst): 
	for i in range(len(lst)): 
		print (lst[i], end=" ") 

#  checking program
if __name__ == '__main__': 
    lst = [12,11,13,5,6]  
    insertionSortRecursive(lst) 
    printArray(lst) 
