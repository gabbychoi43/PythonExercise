import sys


sys.stdin=open('SWEA4013','r')

T=int(input())


def TurnClock(Gear) :

    return [Gear[-1]]+Gear[:-1]
def TurnClockwise(Gear) :

    return Gear[1:]+[Gear[0]]

for t in range(1,T+1) :
    answer=0
    K=int(input())
    Gear=[]
    for i in range(4) :
        Gear.append([int(i) for i in input().split()])

    Oper=[]
    for i in range(K) :
        Oper.append([int(i) for i in input().split()])


    for i in Oper :
        x,y=i

    print('#%d %d' %(t,answer))