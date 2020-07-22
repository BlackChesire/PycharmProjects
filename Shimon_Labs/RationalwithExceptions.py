class Rational:
    def __init__(self,x=0,y=1):
        if not isinstance(x, int):
            raise ValueError("numerator must be an integer", x)
        if not isinstance(y, int):
            raise ValueError("denominator must be an integer", y)
        if y==0:
            raise Exception("can't divide by zero!")
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        if not isinstance(x, int):
            raise ValueError("numerator must be an integer", x)
        self.__x=x
    def setY(self,y):
        if not isinstance(y, int):
            raise ValueError("denominator must be an integer", y)
        if y==0:
            raise ZeroDivisionError()
        self.__y=y
    def isEqual(self,num):
        return self.__x*num.getY()==self.__y*num.getX()
    def mul(self,r):
        t=Rational()
        t.x=self.__x*r.getX()
        t.y=self.__y*r.getY()
        return t
    def div(self,r):
        t=Rational()
        t.x=self.__x*r.getY()
        t.y=self.__y*r.getX()
        return t
    def reduction(self):
        for i in range(2,min(self.__x,self.__y)+1):
            if(self.__x%i==0 and self.__y%i==0):
                self.__x//=i
                self.__y//=i
    def __str__(self):
        return '(%d/%d)'%(self.__x,self.__y)

def main():
    try:
        a=Rational(24)
        a.setY(0)
        print(a)
    except ZeroDivisionError:
        print("Cant divide by zero!")
    except Exception as error:
            print(error)

main()


