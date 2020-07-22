dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict1.items())

double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)


dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)

dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
print(dict1_cond)

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2   
                                                if v%2 == 0}
print(dict1_doubleCond)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 
                                    if v%2 == 0 if v%3 == 0}
print(dict1_tripleCond)

dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(dict1_tripleCond)
