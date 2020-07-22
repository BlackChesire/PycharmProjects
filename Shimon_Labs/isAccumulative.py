
def isAccumulative(lst):
	# small series are not accumulative 
	if len(lst)<3:
		return 0

	# stopping condition 
	if len(lst)==3:
		return (1 if lst[0]+lst[1]==lst[2] else 0)

	# recursive check 
	if (lst[0]+lst[1]==lst[2] and isAccumulative(lst[1:])):
		return 1
	
	return 0


def main():
	lst=[1,2,3,5,8,13,21,34]
	print("it is%s an accumolative list"%("" if isAccumulative(lst)  else "not"))

main()
