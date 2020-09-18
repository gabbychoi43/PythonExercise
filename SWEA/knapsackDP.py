
import sys

sys.stdin=open('')



def solution(weight,Value,W) :

    n=len(weight)
    K=[[0 for i in range(W+1)] for i in range(n+1)]

    for i in range(1,n+1) :
        for w in range(W+1) :
            if i==0 or w==0 :
                K[i][w]=0
            if weight[i-1]>w :
                K[i][w]=K[i-1][w]
            if weight[i-1]<=w :
                K[i][w]=max(K[i-1][w-weight[i-1]]+Value[i-1],K[i-1][w])
    print(K)
    print(K[n][W])

solution([5,4,6,3],[10,40,30,50],10)

