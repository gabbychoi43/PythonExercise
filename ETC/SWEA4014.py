import sys

sys.stdin=open('sample_input4014.txt','r')

T=int(input())

class Runway() :

    def __init__(self,X,Map):
        self.X=X
        self.Map=Map
        self.N=len(Map)


    def DetRunway(self,row):
        before=row[0]
        cnt=1
        for i in range(1,len(row)) :
            if before>row[i] :
                if abs(before-row[i])>1 :
                    return False
                else :
                    if i+self.X>self.N :
                        return False
                    else :
                        for j in range(i,i+self.X) :
                            if row[j]!=row[i] :
                                return False
                        cnt=-self.X+1
            elif before<row[i] :
                if abs(before-row[i])>1 :
                    return False
                else :
                    if abs(before-row[i])==1 :
                        if cnt>=self.X :
                            cnt=1
                        else :
                            return False
            else :
                cnt+=1
            before = row[i]

        return True

    def CountRunway(self):
        Map2=list(map(list, zip(*self.Map)))
        cnt=0
        for i in self.Map :
            if self.DetRunway(i) :
                cnt+=1
        for i in Map2 :
            if self.DetRunway(i) :
                cnt+=1

        return cnt


for test_case in range(1,T+1) :
    N,X=map(int,input().split())
    Map=[]
    for i in range(N) :
        Map.append([int(k) for k in input().split()])

    runway=Runway(X,Map)
    print('#{}'.format(test_case),runway.CountRunway())