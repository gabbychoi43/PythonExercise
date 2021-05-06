import sys
import itertools as it
import copy

sys.stdin=open('sample_input2112.txt','r')

class FilmDet() :

    def __init__(self,K,D,W):
        self.K=K
        self.D=D
        self.W=W

    def Determine(self,Film):
        newFilm=list(map(list, zip(*Film)))

        cnt=0
        for i in range(self.W) :
            for j in range(self.D-self.K+1) :
                if newFilm[i][j:self.K+j]==[0]*self.K or newFilm[i][j:self.K+j]==[1]*self.K :
                    cnt+=1
                    break
            if i+1!=cnt :
                return False
        return cnt==self.W


    def Choose(self,N):
        X=it.combinations(range(self.D),N)
        S=it.product((0,1),repeat=N)
        new={}
        S=[j for j in S]
        for i in X :
            new[i]=S
        return new


    def FilmTest(self,Film):
        if self.Determine(Film)==True :
            return 0
        else :
            X=self.Choose(self.K-1)
            least=self.K
            for key,value in X.items() :
                for x in value :
                    temp=copy.deepcopy(Film)
                    for n in range(len(x)) :
                        temp[key[n]]=[x[n]]*self.W
                        if self.Determine(temp)==True :
                            if least>n+1 :
                                least=n+1

        return least











T=int(input())

for test_case in range(1,T+1) :
    D,W,K=map(int,input().split())
    Film=[]
    for i in range(D) :
        Film.append([int(k) for k in input().split()])


    filmdet=FilmDet(K,D,W)

    print('#{}'.format(test_case),filmdet.FilmTest(Film))

