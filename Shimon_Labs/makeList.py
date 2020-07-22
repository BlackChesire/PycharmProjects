def makeList1(n):
     # Nested list naive
    lst1 = []
    for i in range(2, n+2):
        lst2 = []
        for j in range(1, i):
            lst2.append(j)
        lst1.append(lst2)
    return lst1

def makeList2(n):
    # Nested list comprehension 
    lst = [[j for j in range(1, i+1)] for i in range(1, n+1)] 
    return lst
        
def makeList3(n):
     # Nested list comprehension 
    temp = [i for i in range(1, n+1)]
    
    lst = [temp[:i] for i in range(1, n+1)]
    return lst

#checking program
print(makeList3(3))