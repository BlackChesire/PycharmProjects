# Program to read a text file into a list

fp = open("text.txt","r")
lines = fp.read().split("\n")
print(lines)


# option #2
# data = open("text.txt").readlines()

# option 3
#data = []
#
#for i in open("text.txt"):
#    data.append(i)
#
#print(data)
#
##removing the '\n' charcter from the end of each line
#for i in range(len(data)):
#    if data[i][-1] == '\n':
#        data[i] = data[i][:-1]
        

# option 4
# for i in range(len(data)):
#     data[i] = data[i].strip()

#print(data)

"""  RUN DEMO
['one two\n', 'town city\n', 'big small']
['one two', 'town city', 'big small']
"""