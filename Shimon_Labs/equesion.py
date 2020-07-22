import math
func=lambda a,b,c:{(-b+math.sqrt(b*b-4*a*c))/2*a,(-b-math.sqrt(b*b-4*a*c))/2*a}
def funki(fun,a,b,c):
    d=math.pow(b,2)-4*a*c
    if d>=0:
        return fun(a,b,c)
    print('no solution')
print(funki(func,1,-2,-5))
        
