# Program to build a list of an input numbers in a increasing order until a number is repeated

numbers = []
while True:
    n=int(input('Enter an integer: '))
    i=0
    while i<len(numbers) and numbers[i]<n: i+=1
    if i==len(numbers):
        numbers.append(n)
    elif numbers[i]>n:
        numbers.insert(i,n)
    else:
        break
    print(numbers)

    