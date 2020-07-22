#Program to print all numbers in a given range with an even digits only

def evenDigitsNum1(num):
    #checks if num is made only by even digits - Naive
    while num:
        if (num%10)%2==1:
            return 0
        num//=10
    return 1

def evenDigitsNum2(num):
    #checks if num is made only by even digits - List comprehension
    lst = [int(i) for i in str(num)]
    return all((i%2)==0 for i in lst)

#checking program
ls=list(range(17,1000))
n=[num for num in ls if evenDigitsNum2(num)==1]
print(n)
