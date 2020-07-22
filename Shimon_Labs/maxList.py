# Program to creat a list with the biggest elements of 2 givven lists

def maxList(lst1, lst2):
    return [lst1[i] if lst1[i]>lst2[i] else lst2[i] for i in range(len(lst1)) ]
    
#checking program
print(maxList([2,1,2,1,2], [1,2,1,2,1]))