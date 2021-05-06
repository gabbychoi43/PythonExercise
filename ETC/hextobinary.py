import sys
sys.stdin = open("hextobi", "r")

T = int(input())
for test_case in range(1, T + 1):
    Dic={}
    X=[str(i) for i in range(10)]+['A','B','C','D','E','F']
    N=[]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                for l in range(2) :
                    N.append(str(i)+str(j)+str(k)+str(l))
    for i in range(16) :
        Dic[X[i]]=N[i]
    answer=''
    n,hex=input().split()
    for i in hex :
        answer+=Dic[i]

    print('#%s %s'%(test_case,answer))
