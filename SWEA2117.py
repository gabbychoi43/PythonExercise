import sys

sys.stdin=open('sample_input2117.txt','r')


def dist(xy,x2y2,C) :
    x1,y1=xy
    x2,y2=x2y2

    det=abs(x1-x2)+abs(y1-y2)
    if det<C :
        return True
    return False

class Security() :

    def __init__(self,M,N,Map):
        self.M=M
        self.N=N
        self.Benefit=0
        self.cnt=0
        self.Map=Map

    def detBenefit(self,loc):
        x,y=loc
        for m in range(1,self.N+self.N//2) :
            cnt=0
            cnt2=2*m*m-m*2+1
            for i in range(-m-1,m+1) :
                for j in range(-m-1,m+1) :
                    l,n=x+i,y+j
                    if 0<=l<self.N and 0<=n<self.N :
                        if dist(loc,(l,n),m) :
                            if self.Map[l][n]==1 :
                                cnt+=1

            if 0<=cnt*self.M-cnt2 :
                if self.cnt<cnt :
                    self.cnt=cnt



T=int(input())

for test_case in range(1,T+1) :

    N,M=map(int,input().split())
    Map=[]
    for i in range(N) :
        Map.append([int(k) for k in input().split()])

    security=Security(M,N,Map)
    for i in range(N) :
        for j in range(N) :
            security.detBenefit((i,j))
    print(security.cnt)
