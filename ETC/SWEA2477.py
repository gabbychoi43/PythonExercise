import sys
import queue
sys.stdin=open('sample_input2477.txt','r')




T = int(input())

for test_case in range(1,T+1) :
    N,M,K,A,B=map(int,input().split())
    A-=1
    B-=1
    ReceptionDesk=[int(i) for i in input().split()]
    Recpn=[None]*N
    recpnum=0
    RepairDesk =[int(i) for i in input().split()]
    Repairn=[None]*M
    repairnum=0
    Peoples=[int(i) for i in input().split()]
    waiting1=[]
    waiting2=[]
    subres=[False]*(K+1)
    Time=0
    idx=1
    result=0
    while Peoples or Recpn or waiting2 :

        while Peoples and Peoples[0]==Time :
            Peoples.pop(0)
            waiting1.append(idx)
            idx+=1

        for i in range(N) :
            if Recpn[i] :
                Recpn[i][1]-=1
                if not Recpn[i][1] :
                    waiting2.append(Recpn[i][0])
                    Recpn[i]=None
                    recpnum-=1

        for i in range(N) :
            if Recpn[i] is None :
                if waiting1 :
                    x=waiting1.pop(0)
                    Recpn[i]=[x,ReceptionDesk[i]]
                    recpnum +=1
                    if i==A :
                        subres[x]=True

        for i in range(M) :
            if Repairn[i] :
                Repairn[i][1]-=1
                if not Repairn[i][1] :
                    Repairn[i]=None
        for i in range(M) :
            if Repairn[i] is None :
                if waiting2 :
                    x=waiting2.pop(0)
                    Repairn[i]=[x,RepairDesk[i]]

                    if i==B and subres[x] :
                        result+=x


        Time+=1
    if not result:
        result = -1

    print('#{} {}'.format(test_case, result))