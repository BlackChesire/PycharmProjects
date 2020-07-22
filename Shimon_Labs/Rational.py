class Rational:
    def __init__(self,x=0,y=1):
            self.x=x
            self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def isEqual(self,num):
        return self.x*num.getY()==self.y*num.getX()
    def mul(self,r):
        t=Rational()
        t.x=self.x*r.getX()
        t.y=self.y*r.getY()
        return t
    def div(self,r):
        t=Rational()
        t.x=self.x*r.getY()
        t.y=self.y*r.getX()
        return t
    def reduction(self):
        for i in range(2,min(self.x,self.y)+1):
            if(self.x%i==0 and self.y%i==0):
                self.x//=i
                self.y//=i
    def __str__(self):
        return '(%d/%d)'%(self.x,self.y)

def main():
    a=Rational(2,3)
    b=Rational(4,7)
    print(a.div(b))
main()


