def func(lst):
    n=len(lst)
    if n == 1:
        return (lst[0]);
    
    a = func (lst[:n//2])
    b = func (lst[n//2:])
    if a > b:
        return a
    return b

#  checking program
def main():
    lst = [4,8,1,2,5]
    print(lst)
    print(func(lst))

main()