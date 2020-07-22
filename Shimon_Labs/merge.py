# Program to merge 3 sorted lists

def merge2(lst1,lst2):
    result=[]
    i=j=0
    while i<len(lst1) and j<len(lst2):
        if lst1[i]<lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    if i<len(lst1):
            result.extend(lst1[i:])
    if j<len(lst2):
            result.extend(lst2[j:])
    return result

def merge3(ls1,ls2,ls3):
    return merge2(ls1,merge2(ls2,ls3))

def main():
    l1=[2,4,7,9,14,15,20,27]
    l2=[1,2,3,17]
    l3=[8,18,19,56]
    print(merge3(l1,l2,l3))
main()
