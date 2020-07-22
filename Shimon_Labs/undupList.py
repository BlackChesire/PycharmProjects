# Program to create a new nasted list out of a given one without duplicated elements

def undupList(lst):
    #return [list(set(i)) for i in lst]
    nlls=[]
    for row in lst:
        s=set()
        for i in row:
            s.add(i)
        #temp=list(s)
        temp=[]
        for i in s:
            temp.append(i)
            
        nlls+=[temp]
    return nlls 

# checking program
ls=[[4,6,4,8,6,8,4,2,5],[4,5,6,5,5,5,5,5],[2,44,3,2,44,2,5,8,6,5,6]]
print(undupList(ls))

"""    RUN DEMO
[[2, 4, 5, 6, 8], [4, 5, 6], [2, 3, 5, 6, 8, 44]]
"""


    
