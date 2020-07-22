# Program to find the shortest input string

list = []
str = ""
while True:
    str = input("enter a string: ")
    if(str == "quit"): 
        break;
    list.append(str)
# print(min(list, key=len))
shortest = list[0];
for item in list:
    if len(shortest) > len(item):
        shortest = item
print(shortest)