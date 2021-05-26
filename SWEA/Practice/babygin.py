import sys




sys.stdin=open('Babygin','r')

def babygin(A,B) :

    for i in range(8) :
        if A[i]*A[i+1]*A[i+2]>0 :
            return 1
        if B[i]*B[i+1]*B[i+2]>0 :
            return 2
    for i in range(10) :
        if A[i]>=3 :
            return 1
        if B[i]>=3 :
            return 2


    return 0


T=int(input())

for test_case in range(1,T+1) :
    A={}
    B={}
    for i in range(10) :
        A[i]=0
        B[i]=0
    Card=list(map(int,input().split()))
    for i in range(12) :
        if i%2==0 :
            A[Card[i]]+=1
        else :
            B[Card[i]]+=1
        if babygin(A,B) :
            print('#%d %d'%(test_case,babygin(A,B)))
            break
    if not babygin(A,B) :
        print('#%d %d' %(test_case,0))