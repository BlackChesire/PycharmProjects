# Program 


def unique(lst):
    ret_lst=[]
    for i in range(len(lst)):
        if not lst[i] in lst[:i]:
            ret_lst.append(lst[i])
    return ret_lst

l=[1,2,1,3,2,5,3,6,5,7,4,8,8]
m=[7,5,3,1,9,1,0,4,4]
print(unique(l))

def intersection(lst1,lst2):
    ret_lst=[]
    for n in lst1:
        if n in lst2:
            ret_lst.append(n)
            
    return unique(ret_lst)

print(intersection(l,m))    

def union(lst1,lst2) :
    return unique(lst1+lst2)

print(union(l,m))