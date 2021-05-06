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
                    self.cells[(i,j)]['Power']=cell[i][j]
                    self.cells[(i,j)]['Time']=0
                    self.cells[(i,j)]['activity']=0


    def cell_culturing(self):
        new={}
        d=[(1,0),(0,1),(-1,0),(0,-1)]

        for key,value in self.cells.items() :
            if value['activity']==0 :
                continue
            if value['activity']==1 :
                nkey=[]

                for i in d :
                    nkey.append((key[0]+i[0],key[1]+i[1]))

                for x in nkey :
                    if x not in self.cells :
                        try :
                            new[x].append(value['Power'])
                        except :
                            new[x]={}
                            new[x]['Power']=[value['Power']]

        for key,value in new.items() :
            value['Power']=max(value['Power'])
            value['activity']=0
            value['Time']=0

        for key,value in self.cells.items() :
            new[key]=value
            new[key]['Time']+=1

        for key,value in new.items() :
            if value['Time']==value['Power'] :
                value['activity']=1
            if value['Time']==value['Power']*2 :
                value['activity']=-1

        self.cells=new



T=int(input())

for test_case in range(1,T+1) :
    N,M,K=map(int,input().split())

    c=[]

    for i in range(N) :
        c.append([int(k) for k in input().split()])

    Cells=cells()
    Cells.cells_setting(c,N,M)
    for i in range(K) :
        Cells.cell_culturing()
    cnt=0
    for k,value in Cells.cells.items() :
        if value['activity']!=-1 :
            cnt+=1
    print('#{} {}'.format(test_case,cnt))

