# Program to print the fibonacci series of an input length

def fibo(n):
    if n < 0:
        return -1
    if n==0:
        return 
    f1 = f2 = 1
    if n == 1:
        print(f1)
    else:
        print(f1, f2, end=' ')
    while n > 2:
        f3 = f1+f2
        f1 = f2
        f2=f3
        print(f3, end=' ')
        n -=1
    print()
  
    
    
n= int(input("Please enter a number: "))
ret = fibo(n)
if ret == -1:
    print("ERROR")