import sys

sys.stdin=open('SWEA1263')
T=int(input())

for t in range(1,T+1) :

    answer=0
    L=[int(i) for i in input().split()]
    N=L[0]
    L=L[1:]
    print(N)
    Graph=[]
    for i in range(N) :
        Graph.append(L[i*N:N+i*N])

    for i in range(N) :
        for j in range(N) :
            for k in range(N) :
                if Graph[i][k]*Graph[k][j]>0 :
                    if i!=j :
                        if Graph[i][j]==0 :
                            Graph[i][j]=min(Graph[i][k]+Graph[k][j],2e9)
                        else :
                            Graph[i][j]=min(Graph[i][k]+Graph[k][j],Graph[i][j])
    if t==2 :
        for i in Graph :
            print(i)



    print('#%d %d' %(t,answer))