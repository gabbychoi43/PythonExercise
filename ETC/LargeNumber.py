
import sys

sys.stdin=open('LargeNumber','r')

T=int(input())


for t in range(1,T+1) :

    N,M,K=map(int,input().split())
    Numbers=[int(i) for i in input().split()]

    Numbers.sort()
    X=Numbers.pop()
    Y=Numbers.pop()
    temp=0
    answer=0
    Subsequenc=K*X+Y
    Q=M//(K+1)
    R=M%(K+1)




    print(Q*Subsequenc+R*X)