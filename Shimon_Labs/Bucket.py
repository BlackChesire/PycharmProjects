class Bucket:
    def __init__(self,capacity,currentAmount):
        self.capacity=capacity
        self.currentAmount=currentAmount
    def empty(self):
        self.currentAmount=0
    def isEmpty(self):
        return self.currentAmount==0
    def fill(self,amount):
        if self.capacity-self.currentAmount>=amount:
            self.currentAmount+=amount
            return amount
        else:
            dif=self.capacity-self.currentAmount
            self.currentAmount=self.capacity
            return dif
    def getCapacity(self):
        return self.capacity
    def getCurrentAount(self):
        return self.currentAmount
    def pourInto(self,buck):
        dif=self.fill(buck.currentAmount)
        buck.currentAmount=buck.currentAmount-dif
    def __repr__(self):
        return 'CAPACITY=%.2f   CURRENT AMOUNT=%.2f'%(self.capacity,self.currentAmount)
    
def sorted(lsb):
    for i in range(len(lsb)-1):
        ind=i
        for j in range(i+1,len(lsb)):
            if (lsb[j].capacity-lsb[j].currentAmount)<(lsb[ind].capacity-lsb[ind].currentAmount):
                ind=j
        temp=lsb[i]
        lsb[i]=lsb[ind]
        lsb[ind]=temp
def main():
    import random
    lsb=[]
    for i in range(3):
        c=float(input('הקלד קיבולת דלי'))
        ca=random.randint(1,c)*(random.random())
        b=Bucket(c,ca)
        lsb.append(b)
    print(lsb)
    print('')
    sorted(lsb)
    print(lsb)
    
main()