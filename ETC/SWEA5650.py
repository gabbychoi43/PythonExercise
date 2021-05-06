import sys
sys.stdin=open('sample_input5650.txt','r')

T=int(input())

class pinball() :
    def __init__(self) :
        self.Map=Map
        self.Board={}
        self.score=0
        self.Direction=[(-1,0),(1,0),(0,-1),(0,1)]
        self.WormHole={}
        self.Startable=[]

    def Set_Game(self,Map):
        self.Map=Map
        for i in self.Map :
            i.insert(0,5)
            i.append(5)
        self.Map.insert(0,[5 for i in range(len(Map)+2)])
        self.Map.append([5 for i in range(len(Map)+1)])

        for i in range(len(Map)) :
            for j in range(len(Map)) :
                self.Board[(i,j)]=Map[i][j]
                if Map[i][j]==0 :
                    self.Startable.append((i,j))
                if Map[i][j]>=6 and Map[i][j]<=10 :
                    try :
                        self.WormHole[Map[i][j]].append((i,j))
                    except :
                        self.WormHole[Map[i][j]]=[(i,j)]

    def Switch(self,nloc,X):
        l=self.WormHole[X]
        if nloc==l[0] :
            return l[1]
        else :
            return l[0]


    def Turn(self,block,X):
        if block==1 :
            if X==self.Direction[0] :
                return (1,0)
            elif X==self.Direction[1] :
                return (0,1)
            elif X==self.Direction[2] :
                return (-1,0)
            else :
                return (0,-1)

        elif block==2:
            if X==self.Direction[0] :
                return (0,1)
            elif X==self.Direction[1] :
                return (-1,0)
            elif X==self.Direction[2] :
                return (1,0)
            else :
                return (0,-1)
        elif block==3:
            if X==self.Direction[0] :
                return (0,-1)
            elif X==self.Direction[1] :
                return (-1,0)
            elif X==self.Direction[2] :
                return (0,1)
            else :
                return (1,0)
        elif block==4:
            if X==self.Direction[0] :
                return (1,0)
            elif X==self.Direction[1] :
                return (0,-1)
            elif X==self.Direction[2] :
                return (0,1)
            else :
                return (-1,0)
        else :
            if X==self.Direction[0] :
                return (1,0)
            elif X==self.Direction[1] :
                return (-1,0)
            elif X==self.Direction[2] :
                return (0,1)
            else :
                return (0,-1)


    def Move(self,Startloc,Direction):
        score=0
        x,y=Startloc
        Dir=Direction
        while True :


            nloc=(x+Dir[0],y+Dir[1])
            if nloc==Startloc :
                break
            X=self.Board[nloc]
            if X==-1 :
                break
            if X>=1 and X<=5 :
                score+=1
                Dir=self.Turn(X,Dir)

            if X>=6 and X<=10 :
                nloc=self.Switch(nloc,X)
            x,y=nloc

        return score

    def Start_Game(self) :
        for i in self.Startable :
            for j in self.Direction :
                if self.Move(i,j)>self.score :
                    self.score=self.Move(i,j)

        return 0








for test_case in range(1,T+1) :
    N=int(input())
    Map=[]
    for i in range(N) :
        Map.append([int(i) for i in input().split()])
    Pinball=pinball()

    Pinball.Set_Game(Map)
    Pinball.Start_Game()
    print('#{} {}'.format(test_case,Pinball.score))


