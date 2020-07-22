# Program to Check if a nested list is a subset of another nested list 

def checkSubset1(lst1, lst2): 
    exist = True
    for i in lst2: 
        if i not in lst1: 
            exist = False
    return exist 

def checkSubset2(lst1, lst2): 
	temp1 = [] 
	temp2 = [] 
	for i in lst1: 
		temp1.append(tuple(i)) 
	for i in list2: 
		temp2.append(tuple(i)) 
	
	return set(temp2) < set(temp1) 

def checkSubset3(lst1, lst2): 
    return all(x in lst1 for x in lst2) 
	
#checking program
list1 = [[2, 3, 1], [4, 5], [6, 8]] 
list2 = [[4, 5], [6, 8]] 
print(checkSubset1(list1, list2)) 
print(checkSubset2(list1, list2)) 
print(checkSubset3(list1, list2)) 
