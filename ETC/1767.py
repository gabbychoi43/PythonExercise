import sys

sys.stdin=open('1767', 'r')

T=int(input())

for t in range(1,T+1) :
    N=int(input())
    Map=[]

    for j in range(N) :

        L=[int(i) for i in input().split()]
        Map.append(L)
    Maxinos=[]
    for i in range(N) :
        for j in range(N) :
            if Map[i][j]==1 :
                Maxinos.append((i,j))
                
