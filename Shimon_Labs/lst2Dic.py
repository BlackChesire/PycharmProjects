# Program to create a dictionaty from 2 lists

def lst2Dic(lst1, lst2):
    dic = {}
    if len(lst1) > len(lst2):
        return dic
    for i in range(len(lst1)):
        dic[lst1[i]] = lst2[i]
    return dic
    #return {lst1[i]:lst2[i] for i in range(len(lst1) }
    #return {k:v for (k,v) in zip(lst1,lst2)}

l1 = [1,2,3]
l2 = ['a','b','c']
print(lst2Dic(l1,l2))

