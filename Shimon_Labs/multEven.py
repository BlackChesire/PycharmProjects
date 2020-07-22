def  multEven(lst):
	res=1

	if len(lst) == 0:
		return res
	if lst[0]%2 == 0:
		res=lst[0]
	return res*multEven(lst[1:])


def main():
    lst = [1,2,3,4,5,6,7,8]
    print(multEven(lst))
    
main()