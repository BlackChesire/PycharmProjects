# Python program for implementation of Bubble Sort

def bubbleSort(lst):
	n = len(lst)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if lst[j] > lst[j+1] :
				lst[j], lst[j+1] = lst[j+1], lst[j]


# testing program
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print ("Sorted array is:",arr)
