
class curruption() :

    def __init__(self,graph,currupted):
        self.total=0
        self.graph=graph
        self.currpted=currupted
        self.child=[0]
        self.currptednum=0


    def search(self,n):
        candidate=[]
        m=-2e9
        cleardata=0
        for i in self.child :
            try :
                candidate+=self.graph[i]
            except :
                continue
        for i in candidate :
            self.BFS(i)
            if self.total>m :
                cleardata=i
                m=self.total
            self.total=0
        self.Clearnode(cleardata)
        candidate.remove(cleardata)
        ncandidate=[]
        for i in candidate :
            try :
                ncandidate+=self.graph[i]
            except :
                continue
        print(ncandidate)
        for i in ncandidate :
            self.search(i)

        return 0

    def Clearnode(self,n):

        if not n in self.graph :
            return 0
        x=self.graph[n]
        del(self.graph[n])

        for i in x :
            self.Clearnode(i)

    def BFS(self,n):
        if not n in self.graph :
            return 0
        self.total+=len(self.graph[n])
        for i in self.graph[n] :
            self.BFS(i)



def solution(n,edges) :
    graph={}
    for i in edges :
        p,c=i
        try :
            graph[p].append(c)
        except :
            graph[p]=[c]
    currupted={0:True}
    for i in range(1,n) :
        currupted[i]=False
    Network=curruption(graph,currupted)
    Network.search(0)

    print(Network.graph)

solution(19,[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]])