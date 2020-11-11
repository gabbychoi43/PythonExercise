
import sys
sys.stdin=open('Happybox','r')



T=int(input())

for t in range(1,T+1) :

    W,N=map(int,input().split())
    weight=[]
    value=[]
    for i in range(N) :
        w,v=map(int,input().split())
        weight.append(w)
        value.append(v)

    K=[[0 for i in range(W+1)] for i in range(N+1)]


    for i in range(1,N+1) :
        for w in range(W+1) :
            if i==0 or w==0 :
                K[i][w]=0
            if weight[i-1]>w :
                K[i][w]=K[i-1][w]
            if weight[i-1]<=w :
                K[i][w]=max(K[i-1][w-weight[i-1]]+value[i-1],K[i-1][w])
    print('#%d %d'%(t,K[N][W]))