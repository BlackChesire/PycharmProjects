# Program to flatten only elemnts shorten than 6 chars in a nasted list

def flattenLst6a(mat):
    # Nested List Naive
    flatten = [] 
      
    for sublist in mat: 
        for s in sublist: 
              
            if len(s) < 6: 
                flatten.append(s) 
    return flatten

def flattenLst6b(mat):
    # Nested List comprehension
    return [planet for sublist in planets for planet in sublist if len(planet) < 6] 
 
       
#checking program
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
print(flattenLst6b(planets)) 
  
   