def findNumInList(lst, num):
    if len(lst)==0:
        return -1
    if lst[0] == num:
        return 1
    pos = findNumInList(lst[1:],num)
    if pos==-1:
        return -1
    return pos+1
    

def main():
    l = [1,2,3,4,5,6,7,8]
    n = 9
    res = findNumInList(l,n)
    if res==-1:
        print(n, "is not in the list!")
    else:
        print("the index of %d in the list is: %d"%(n, res))
    
main()
