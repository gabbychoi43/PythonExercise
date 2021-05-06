import sys

sys.stdin=open('sample_inputPipe.txt','r')

class Pipe() :

    def __init__(self,Map):
        self.Map=Map
        self.loc=[(0,0),(0,1)]
        self.cnt=0



    def DFS(self,step):
        if step==N*N :
            return 0
        dx = [0, 1, 1]
        dy = [1, 1, 0]
        for i in range(3):
            x, y = self.loc[1]
            m,n=self.loc[0]
            det=(x-m,y-n)
            if m==n and i!=1 :
                continue
            elif m>n and i==0 :
                continue
            elif m<n and i==3 :
                continue

            nloc = (x + dx[i], y + dy[i])
            if 0<=nloc[0]<N and 0<=nloc[1]<N :
                if self.Map[nloc[0]][nloc[1]]==1 :
                    continue
                if m==n :
                    if self.Map[x+1][y]==1 or self.Map[x][y+1]==1 or self.Map[x+1][y+1]==1 :
                        continue
                if nloc == (N-1, N-1):
                    self.cnt+=1
                else :
                    self.loc=[nloc,(x,y)]
                    self.DFS(step+1)


T=int(input())
for test_case in range(1,T+1) :
    N=int(input())
    Map=[]
    for i in range(N) :
        Map.append([int(k) for k in input().split()])

    pipe=Pipe(Map)
    pipe.DFS(0)
    print('#{}'.format(test_case),pipe.cnt)





