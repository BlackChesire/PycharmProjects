# program to calculate the sum of numbers in a list

def listSum(numList):
    if len(numList) == 0:
        return 0
    else:
        return numList[0] + listSum(numList[1:])
        
print(listSum([2, 4, 5, 6, 7]))