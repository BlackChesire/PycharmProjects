# Program to read a text file into a list

# option 1
#data = open("text.txt").read().split('\n')

data = []
for i in open("text.txt"):
    data.append(i)

print(data)

#removing the '\n' charcter from the end of each line
for i in range(len(data)):
    if data[i][-1] == '\n':
        data[i] = data[i][:-1]

# or
# for i in range(len(data)):
#     data[i] = data[i].strip()

print(data)

"""  RUN DEMO
['one two\n', 'town city\n', 'big small']
['one two', 'town city', 'big small']
"""