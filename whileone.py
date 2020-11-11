import sys

sys.stdin=open('whileone','r')

T=int(input())

for t in range(1,T+1) :

    N,K=map(int,input().split())
    step=0

    while True:
        if N==1 :
            break

        if N%K==0 :
            N=N//K
            step+=1
        else :
            N-=1
            step+=1

    print(step)
