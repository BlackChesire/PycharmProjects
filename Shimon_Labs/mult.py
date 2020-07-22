def mult(a,b):
    if a == 1:
        return b
    return b+mult(a-1,b)
        
def main():
    print(mult(3,5))
    
main()