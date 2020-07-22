# Program for implementation of recursive mergeSort 

def mergeSort(lst): 
	if len(lst) >1: 
		mid = len(lst)//2 #Finding the mid of the array 
		lstL = lst[:mid] # Dividing the array elements 
		lstR = lst[mid:] # into 2 halves 

		mergeSort(lstL) # Sorting the first half 
		mergeSort(lstR) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(lstL) and j < len(lstR): 
			if lstL[i] < lstR[j]: 
				lst[k] = lstL[i] 
				i+=1
			else: 
				lst[k] = lstR[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(lstL): 
			lst[k] = lstL[i] 
			i+=1
			k+=1
		
		while j < len(lstR): 
			lst[k] = lstR[j] 
			j+=1
			k+=1

def f(s):
	if s=='':
		return ''
	else:
		return f(s[1:])+s[-1]
print(f('abcde'))