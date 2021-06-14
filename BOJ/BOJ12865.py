import sys

sys.stdin=open('BOJ12865','r')

N,K=map(int,input().split())

DP=[[0]*(K+1) for i in range(N)]

items=[]
for i in range(N) :
    x,y=map(int,input().split())
    items.append((x,y))

for i in range(N) :
    for j in range(K+1) :
        if items[i][0]>j :
            DP[i][j]=DP[i-1][j]
        else :
            DP[i][j]=max(DP[i-1][j-items[i][0]]+items[i][1],DP[i-1][j])
for i,j in enumerate(DP) :
    print(items[i],j)
