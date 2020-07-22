# Program to check if a number is divided by 3

def sumDigit(num):
    if num<10:
        return num
    return num%10 + sumDigit(num//10)

def div3(num):
    if num in [0,3,6,9]:  #n==0 |n==3 | n==6 | n==9
        return 1
    if num<10:
        return 0
    #return div3(sumDigit(num))
    return div3( sum(int(i) for i in str(num)))

def main():
	n=int(input("Please enter a number:"))
	print("%d can%s be devided by 3"%(n, "" if div3(n)==1 else " not"))
	
main()
