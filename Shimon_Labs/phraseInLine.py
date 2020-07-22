# Program to find all the lines in a file containing an input phrase

inp=open('ab40thv.txt','r')
content = inp.readlines()
inp.close()
phrase = input('Enter phrase: ')
lines_with_phrase=[]
for line in content:
    if phrase in line:
        lines_with_phrase.append(line)
        lines_with_phrase.append('=============\n')

for line in lines_with_phrase:
    print(line,end='')
