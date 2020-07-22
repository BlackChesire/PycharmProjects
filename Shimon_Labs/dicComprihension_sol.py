dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict1.items())

# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
#{'e': 10, 'a': 2, 'c': 6, 'b': 4, 'd': 8}

dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)
#{'dd': 4, 'ee': 5, 'aa': 1, 'bb': 2, 'cc': 3}

# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}

print(dict1_cond)
#{'e': 5, 'c': 3, 'd': 4}

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)
#{'d': 4}

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}

print(dict1_tripleCond)
#{'f': 6}

# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

print(dict1_tripleCond)
#{'f': 'even', 'c': 'odd', 'b': 'even', 'd': 'even', 'e': 'odd', 'a': 'odd'}