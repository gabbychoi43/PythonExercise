import sys

sys.stdin=open('UDLR', 'r')

T=int(input())

for t in range(1,T+1) :

    N=int(input())

    Direction=list(map(str,input().split()))
    Loc=[1,1]

    for i in Direction :

        if i=='R' :
            if Loc[1]+1 <=5 :
                Loc[1]+=1
        if i=='L' :
            if Loc[1]-1>=1 :
                Loc[1]-=1

        if i=='U' :
            if Loc[0]-1>=1 :
                Loc[0]-=1
        if i=='D' :
            if Loc[0]+1<=5 :
                Loc[0]+=1

    print(Loc[0],Loc[1])
