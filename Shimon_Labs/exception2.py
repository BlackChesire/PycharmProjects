# Attempt to open non-existent file
fname = input("File: ")

try:
    f = open(fname)
    x=5
    x+=1
except:
    print("Error. No this file!")
else:
    print(f.read())