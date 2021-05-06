import sys

sys.stdin=open('sample_input5653.txt','r')

class cells() :

    def __init__(self):
        self.cells={}

    def cells_setting(self,cell,N,M):

        for i in range(N) :
            for j in range(M) :
                if cell[i][j]!=0 :
                    self.cells[(i,j)]={}
                    self.cells[(i,j)]['Live']=True
                    self.cells[(i,j)]['Time']=2*cell[i][j]
                    self.cells[(i,j)]['Power']=[cell[i][j]]
                    self.cells[(i,j)]['Activity']=False



    def culturing(self,K):
        for i in range(K-1) :
            self.reproduction()




    def reproduction(self):
        new={}
        for i,j in self.cells.items() :
            new[i]=j
            new[i]['Time']-=1
            new[i]['Activity']-=1
            if new[i]['Time']==0:
                new[i]['Live']=False
            if new[i]['Activity']==0 :
                new[i]['Activity']==True


        for i,j in self.cells.items() :
            if j['Time']==True and j['Activity']==True :
                x,y=i
                newkey=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                for x in newkey :
                    if x not in self.cells.keys() :
                        try :
                            new[i]['Power'].append(j['Power'])
                        except :
                            new[i]=j

        for i,j in new.items() :
            new[i]['Power']=max(j['Power'])



        self.cells=new



T=int(input())

for test_case in range(1,T+1) :
    N,M,K=map(int,input().split())

    c=[]

    for i in range(N) :
        c.append([int(k) for k in input().split()])

    Cells=cells()
    Cells.cells_setting(c,N,M)
    Cells.culturing(K)
    print('#{} {}'.format(test_case,len(Cells.cells)))

