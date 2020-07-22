"""
program to print outline of rectangle from digits 1-top,
starting from up-left corner.
"""
top=6
length=int(input("enter length of rectangle (number bigger than 1): "))
width=int(input("enter width of rectangle (number bigger than 1): "))


for i in range(length):
    print(i%top +1,end='')
left = (length * 2 + (width - 2) * 2) % top
if left == 0:
    left = top
i+=1
right = i%top +1
for i in range(width - 2):
    print("\n%d"%left, end='')	
    for j in range(length - 2):
        print(' ',end='')
    print(right, end='')	
    right = right %top +1
    if left == 1:
		     left = top
    else:
		     left-=1
print()
for i in range(length):
    print(left, end='')
    if left == 1:
      left=top
    else:
		    left-=1

print()







	




