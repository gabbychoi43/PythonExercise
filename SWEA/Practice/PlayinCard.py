import sys

sys.stdin=open('Playing', 'r')


T=int(input())


for t in range(1,T+1) :

    N,M=map(int,input().split())
    card=[]
    for i in range(N) :
        card.append(list(map(int,input().split())))

    answer=0
    for i in range(N) :
        if min(card[i])>=answer :
            answer=min(card[i])

    print(answer)