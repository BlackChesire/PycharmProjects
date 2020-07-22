def removeMultiples1(number_list,  divnum):
    i=0
    while i < len(number_list):
        if number_list[i] % divnum == 0:
            number_list.pop(i)
        else:
            i+=1

def removeMultiples2(number_list,  divnum):
    new_list = []
    for num in number_list:
        if num % divnum != 0:
            new_list.append(num)
    
    #[:] is required to change the objet itself, and not the reference
    number_list[:] = new_list 


lst = input("Please enter a list of numbers: ").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

num = int(input("Please enter a divaidor: "))
removeMultiples1(lst, num)
print(lst)