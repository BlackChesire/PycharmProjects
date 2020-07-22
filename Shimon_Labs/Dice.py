from random import randrange
class Dice:
    def __init__(self,sides):
        self.sides=sides
        self.value=0
    def roll(self):
        self.value=randrange(1,self.sides+1)
    def getValue(self):
        return self.value
    
def main():
    d1=Dice(6)
    d2=Dice(6)
    count=0
    while(d1.getValue()!=6 or d2.getValue()!=6):
        count+=1
        d1.roll()
        d2.roll()
    print(count)
main()
        
