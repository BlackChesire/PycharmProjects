# Program to generate a list of repeated digit in an input list

def sumlist(numbers):
    result = [0] * 10
    for n in numbers:
        result[n]+=1
    return result

lst = input("Please enter a list of numbers: ").split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

print(sumlist(lst))


"""   RUN DEMO


Please enter a list of numbers: 5 3 4 3 3 2 5
[0, 0, 1, 3, 1, 2, 0, 0, 0, 0]
"""