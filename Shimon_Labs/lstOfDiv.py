# Program to build a list of lists with a divisors of each index


n=int(input('Enter a positive integer: '))

divisors=[[],[1]]
for i in range(2,n+1):
    div=[]
    for j in range(1,i//2+1):
        if i%j==0:
            div.append(j)
    div.append(i)
    divisors.append(div)
print(divisors)

for i in range(1,n+1):
    print('{0:<4}: {1}'.format(i,divisors[i]))