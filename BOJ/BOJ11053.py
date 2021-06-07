import heapq
import sys


sys.stdin=open('BOJ11053','r')


N=int(input())

Sequence=[int(i) for i in input().split()]

answer=0



DP=[0 for i in range(N)]
DP[0]=1
for i in range(1,N) :
    temp=0
    for j in range(i) :
        if Sequence[i]>Sequence[j] :
            temp=max(temp,DP[j])
    DP[i]=temp+1


print(max(DP))

