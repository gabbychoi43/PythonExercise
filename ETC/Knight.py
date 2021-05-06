import sys

sys.stdin=open('Knight','r')

T=int(input())

for t in range(1,T+1) :
    x,y=list(input())
    L=['a','b','c','d','e','f','g','h']

    count=0
    x=L.index(x)
    y=int(y)-1
    d=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    for i in d :
        if 0<=x+i[0]<8 and 0<=y+i[1]<8 :
            count+=1

    print(count)


