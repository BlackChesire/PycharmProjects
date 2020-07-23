class Parent:
    def __init__(self, name, cellNum):
        self.__name = name
        self.__cellNum = cellNum

    def getName(self):
        return self.__name

    def getCellNum(self):
        return self.__cellNum

    def setName(self, name):
        self.__name = name

    def setCellNum(self, cellNum):
        self.__cellNum = cellNum

    def __repr__(self):
        return 'PARENT -> %s:%s' % (self.__name, self.__cellNum)


class Student:
    def __init__(self, sn, name, phonNum, parent):
        self.__sn = sn
        self.__name = name
        self.__phonNum = phonNum
        self.__parent = parent

    def getSn(self):
        return self.__sn

    def getName(self):
        return self.__name

    def getPhonNum(self):
        return self.__phonNum

    def getParent(self):
        return self.__parent

    def setSn(self, sn):
        self.__sn = sn

    def setName(self, name):
        self.__name = name

    def setPhonNum(self, phonNum):
        self.__phonNum = phonNum

    def setParent(self, parent):
        self.__parent = parent

    def __repr__(self):
        return 'STUDENT-> %d:%s:%s\n%s' % (self.__sn, self.__name, self.__phonNum, self.__parent)


class StudentList:
    def __init__(self):
        self.__list = []

    def getList(self):
        return self.__list

    def add(self, stu):
        ind = 0
        while ind < len(self.__list) and stu.getName() > self.__list[ind].getName():
            ind += 1
        self.__list.insert(ind, stu)

    def getStudent(self, sn):
        ind = 0
        for stu in self.__list:
            if stu.getSn() == sn:
                return ind
            ind += 1
        return -1

    def delete(self, sn):
        del (self.__list[self.getStudent(sn)])

    def __str__(self):
        return '%s' % (self.__list)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "x:{0} y:{1}".format(self._x, self._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Line:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    def __str__(self):
        return "{0} | {1}".format(self._p1, self._p2)

    def get_p1(self):
        return self._p1

    def get_p2(self):
        return self._p2

    def slope(self):
        return ((self._p1.get_y() - self._p2.get_y()) / (self._p1.get_x() - self._p2.get_x()))

    def y_intercept(self):
        y = self.slope() * (0 - self._p1.get_x()) + self._p1.get_y()
        if y == 0:
            return None
        return y

    def isParallel(self, Li):
        return Li.slope() == self.slope()


"""
def main():
      p1 = Point(2,4)
      p2 = Point(1,6)
      l2 = Line(p1,p2)
      l = Line(p1,p2)
      print(l.isParallel(l2))

main()
"""