# Program to bucket sort a list

def bucketS(lst, low, high):
    counters=dict()
    for i in range(low, high+1):
        counters[i]=0
    #counters = {i:0 for i in range(low, high+1)}
    for i in lst:
        counters[i]+=1
    nls=[]
    for i in counters:
        for j in range(counters[i]):
            nls.append(i)
    return nls
    
def main():
    l=[80,45,77,52,100,95,67,93,63,36,80,67,100]
    print(bucketS(l,0,101))
    
main() 
