#Program to count the number of lines, words and letters in a text file

lines = 0
words = 0
letters = 0

#text = open("text.txt","r").read()
#lines = len(text.split('\n'))
#words = len(text.split())
#letters = len(text.replace("\n","")


for line in open("ab40thv.txt"):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
