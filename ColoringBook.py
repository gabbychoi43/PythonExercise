def rot(key,N) :
    roted=[]
    for i in range(N) :
        temp=[]
        for j in range(N) :
            temp.append(key[N-1-j][i])
        roted.append(temp)
    return roted

def check(startX,startU,key,lock,expendsize,start,end) :
    return 0



def solution(key, lock):
    M=len(lock)
    N=len(key)
    D=M-N
    rot1=rot(key,N)
    rot2=rot(rot1,N)
    rot3=rot(rot2,N)
    keys=[[0 for i in range(M)] for i in range(M)]
    Keys=[]







    return True

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])