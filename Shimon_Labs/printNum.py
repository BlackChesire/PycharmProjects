def printForward(num):
    if num!=0:
        printForward(num-1)
        print(num,end=' ')
        
def printBackward(num):
    if num!=0:
        print(num,end=' ')
        printBackward(num-1)
                  
def main():
    printForward(7)
    print()
    printBackward(7)
   
main()