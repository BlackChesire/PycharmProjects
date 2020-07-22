#Program to check if a number is symetic

#s1 = input("enter a decimal number: ")
#s1rev = s1[::-1] 
#print("symetric" if s1 == s1rev else "not not symetric ")

n = int(input("Please enter a number: "))
n1=n
n2 = 0

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit

if n==n2:
    print("the number is symetric!")
else:
    print("the number is not symetric!")


"""  RUN DEMO
Please enter a number: 123
the number is not symetric!

Please enter a number: 13531
the number is symetric!
"""