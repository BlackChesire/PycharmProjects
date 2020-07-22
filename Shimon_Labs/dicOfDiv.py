# Program to build a dictionary of dividers from a list of integers

def dicOfDiv(ls):
    sum=0
    count=0
    dic={}
    for i in ls:
        lst=[]
        for j in range(2,i//2+1):
            if i%j==0:
                sum+=j
                count+=1
                lst.append(j)
        dic[i]=lst
    return dic,sum,count


# checking program
l=[12,36,52]
print(dicOfDiv(l))

"""   RUN  DEMO
({12: [2, 3, 4, 6], 36: [2, 3, 4, 6, 9, 12, 18], 52: [2, 4, 13, 26]}, 114, 15)"""

        
