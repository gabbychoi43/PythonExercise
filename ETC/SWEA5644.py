import sys

sys.stdin=open('sample_input5644.txt', 'r')
def dist(xy,x2y2,C) :
    x1,y1=xy
    x2,y2=x2y2

    det=abs(x1-x2)+abs(y1-y2)
    if det<=C :
        return True
    return False
class Charger() :

    def __init__(self,x,y,C,capacity):
        self.range={}
        self.range[(x,y)]=capacity
        self.capacity=capacity
        self.C=C
        self.center=(x,y)

    def setrange(self,x,y):
        for i in range(-self.C,self.C+1) :
            for j in range(-self.C,self.C+1) :
                if dist((x+i,y+j),(x,y),self.C) :
                    self.range[(x+i,y+j)]=self.capacity



class Move() :
    def __init__(self,Chargers):
        self.A=[(1,1)]
        self.B=[(10,10)]
        self.Chargers=Chargers
        self.s=0

    def makeLoc(self,HumanA,HumanB):
        for i in range(len(HumanA)) :
            if HumanA[i]==4 :
                self.A.append((self.A[i][0]-1,self.A[i][1]))
            elif HumanA[i]==3 :
                self.A.append((self.A[i][0],self.A[i][1]+1))
            elif HumanA[i]==2 :
                self.A.append((self.A[i][0]+1,self.A[i][1]))
            elif HumanA[i]==1 :
                self.A.append((self.A[i][0],self.A[i][1]-1))
            else :
                self.A.append(self.A[i])
        for i in range(len(HumanB)) :
            if HumanB[i]==4 :
                self.B.append((self.B[i][0]-1,self.B[i][1]))
            elif HumanB[i]==3 :
                self.B.append((self.B[i][0],self.B[i][1]+1))
            elif HumanB[i]==2 :
                self.B.append((self.B[i][0]+1,self.B[i][1]))
            elif HumanB[i]==1 :
                self.B.append((self.B[i][0],self.B[i][1]-1))
            else :
                self.B.append(self.B[i])

    def Charging(self,M):
        for i in range(len(self.A)) :
            tempA=[(0,0)]
            tempB=[(0,0)]
            locA=self.A[i]
            locB=self.B[i]
            for k in self.Chargers :
                x=k.center
                k=k.range
                if locA in k.keys() :
                    tempA.append((x,k[locA]))
                if locB in k.keys() :
                    tempB.append((x,k[locB]))
            temp=[0]
            for k in tempA :
                for j in tempB :
                    if k[1]!=j[1] :
                        temp.append(k[1]+j[1])
                    elif k[1]==j[1] :
                        if k[0]==j[0] :
                            temp.append(k[1])
                        else :
                            temp.append(2*k[1])

            self.s+=max(temp)














T=int(input())
for test_case in range(1,T+1) :
    M,K=map(int,input().split())

    PA=[int(i) for i in input().split()]
    PB=[int(i) for i in input().split()]
    AP=[]
    for i in range(K) :
        x,y,c,cap=map(int, input().split())
        AP.append(Charger(x,y,c,cap))
        AP[i].setrange(AP[i].center[0],AP[i].center[1])




    humans=Move(AP)
    humans.makeLoc(PA,PB)
    humans.Charging(M)
    print('#{} {}'.format(test_case,humans.s))



