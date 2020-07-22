# program to work with lists
list1 = []
list2 = []
str = ""
print("enter first list:");
while True:
    str = input("")
    if(str == "done"): 
        break;
    list1.append(float(str))

print("enter second list:");
while True:
    str = input("")
    if(str == "done"): 
        break;
    list2.append(float(str))
    
print("intersection")
for x in list1:
    if x in list2:
        print(x, end=' ')
        
print("\ndifference")
for x in list1:
    if x not in list2:
        print(x, end=' ')
        
for x in list2:
    if x not in list1:
        print(x, end=' ')