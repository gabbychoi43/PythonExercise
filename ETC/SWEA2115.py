import sys
import itertools as it

sys.stdin=open('sample_input2115.txt','r')

class HoneyBee() :
    def __init__(self,N,M,C,Map):
        self.benefit=0
        self.Map=Map
        self.N=N
        self.C=C
        self.M=M

    def Choose(self):
        if 2*self.M>self.N :
            X=list(it.combinations(range(N),2))
            return X
        else :
            X=list(it.combinations(range(N),2))
            for i in range(N) :
                X.append((i,i))
            return X

    def ChooseHoney(self,row):
        benefit=0
        for i in range(1,len(row)+1) :
            x=it.combinations(row,i)
            for j in x :
                temp=0
                if  sum(j)<=self.C :
                    for n in j :
                        temp+=n**2
                if temp>benefit :
                    benefit=temp
        return benefit

    def ChooseRow(self,xy):
        x,y=xy
        if x!=y :
            first=self.Map[x]
            firstmax=0
            secondmax=0
            for i in range(self.N-self.M+1):
                if firstmax<=self.ChooseHoney(first[i:i+self.M]) :
                    firstmax=self.ChooseHoney(first[i:i+self.M])
            second=self.Map[y]
            for i in range(self.N-self.M+1):
                if secondmax<=self.ChooseHoney(second[i:i+self.M]) :
                    secondmax=self.ChooseHoney(second[i:i+self.M])
            return firstmax+secondmax
        else :
            Row=self.Map[x]
            firstmax=0
            secondmax=0
            for i in range(self.N-self.M*2) :
                if firstmax<self.ChooseHoney(Row[i:self.M]) :
                    firstmax=self.ChooseHoney(Row[i:self.M])
                for j in (self.M+i,self.N-self.M) :
                    if secondmax<self.ChooseHoney(Row[j:j+self.M]) :
                        secondmax=self.ChooseHoney(Row[j:j+self.M])
            return firstmax+secondmax
















T=int(input())

for test_case in range(1,T+1) :
    solution=0
    N,M,C=map(int,input().split())
    Map=[]
    for i in range(N) :
        Map.append([int(x) for x in input().split()])

    bees=HoneyBee(N,M,C,Map)
    m=0
    for i in bees.Choose() :
        s=bees.ChooseRow(i)
        if m<s :
            m=s





    print('#{}'.format(test_case),m)