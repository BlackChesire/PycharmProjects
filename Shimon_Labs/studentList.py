class Parent:
    def __init__(self,name,cellNum):
        self.__name=name
        self.__cellNum=cellNum
        
    def getName(self):
        return self.__name
    
    def getCellNum(self):
        return self.__cellNum
    
    def setName(self,name):
        self.__name=name
        
    def setCellNum(self,cellNum):
        self.__cellNum=cellNum
        
    def __str__(self):
        return 'PARENT -> %s:%s'%(self.__name,self.__cellNum)
    
class Student:
    def __init__(self,sn,name,phonNum,parent):
        self.__sn=sn
        self.__name=name
        self.__phonNum=phonNum
        self.__parent=parent
        
    def getSn(self):
        return self.__sn
    
    def getName(self):
        return self.__name
    
    def getPhonNum(self):
        return self.__phonNum
    
    def getParent(self):
        return self.__parent
    
    def setSn(self,sn):
        self.__sn=sn
        
    def setName(self,name):
        self.__name=name
        
    def setPhonNum(self,phonNum):
        self.__phonNum=phonNum
        
    def setParent(self,parent):
        self.__parent=parent
        
    def __str__(self):
        return 'STUDENT-> %d:%s:%s\n%s'%(self.__sn,self.__name,self.__phonNum,self.__parent)
        
class StudentList:
    def __init__(self):
        self.__list=[]
    def getList(self):
        return self.__list  
    
    
    
    def add(self,stu):
        ind=0
        while ind<len(self.__list) and stu.getName()>self.__list[ind].getName():
            ind+=1
        self.__list.insert(ind,stu)
        
    def getStudent(self,sn):
        ind=0
        for stu in self.__list:
            if stu.getSn()==sn:
                return ind
            ind+=1
        return -1
    
    def delete(self,sn):
        del (self.__list[self.getStudent(sn)])
        
    def __str__(self):
        s=""
        for i in self.__list:
            s+=str(i)+'\n'
        return s
    
        
        
def main():
    ls=StudentList()
    p1=Parent('toni montana','050-6468849')
    s1=Student(456,'don montana','04-6924248',p1)
    p2=Parent('fabrlko luchiano','050-7676765')
    s2=Student(777,'bombino luchiano','03-6456746',p2)
    p3=Parent('miko pinto','050-6468849')
    s3=Student(892,'lola pinto','04-6924248',p3)
    p4=Parent('fabrlko devinchi','050-7676765')
    s4=Student(926,'zulu devinchi','03-6456746',p4)
    ls.add(s1)
    ls.add(s2)
    ls.add(s3)
    ls.add(s4)
    print(ls)
    ls.delete(456)
    print(ls)
    print(ls.getList()[1])
    
main()
        
        