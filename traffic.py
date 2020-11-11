def solution(lines):
    answer = 0
    n=len(lines)
    L1,L2=[],[]
    for i in lines :
        x=i.split()
        T=x[1]
        S=x[2]
        T=T.split(':')
        T=int(T[0])*3600+int(T[1])*60+float(T[2])
        S=float(S.replace('s',''))
        L=[T,T+S]
        L1.append(T-S)
        L2.append(T)



    for i in range(n) :
        temp=0

        for k in range(i,n) :
            if L1[k]<L2[i]+1 :
                temp+=1

        if temp>=answer:
            answer=temp

    return answer

solution(	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])