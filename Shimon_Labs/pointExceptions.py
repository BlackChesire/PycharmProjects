def checkX(x):
    return x>=0 and x<1920
def checkY(y):
    return y>=0 and y<1080
class Point:
    def __init__(self,x=0,y=0):
        if not checkX(x):
            raise Exception ('wrong value of x(0-1920)')
        if not checkY(y):
            raise Exception ('wrong value of y(0-1080)')
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        if not checkX(x):
            raise Exception ('wrong value of x(0-1920)')
        self.__x=x
    def setY(self,y):
        if not checkY(y):
            raise Exception ('wrong value of y(0-1080)')
        self.__y=y
    def __str__(self):
        return '(%d,%d)'%(self.__x,self.__y)
def main():
    try:
        p1=Point(60,900000)
        print(p1)
    except Exception as error:
        print(error," please try again...")
main()






