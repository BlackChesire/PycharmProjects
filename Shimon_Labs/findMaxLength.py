# Program to Find maximum length list in a nested list 

def findMaxLength(lst): 
	maxList = max((x) for x in lst) 
	maxLength = max(len(x) for x in lst ) 

	return maxList, maxLength 
	
#checking program
lst = [['A'], ['A', 'B'], ['A', 'B', 'C']] 
print(findMaxLength(lst)) 

"""   RUN DEMO
(['A', 'B', 'C'], 3)
"""