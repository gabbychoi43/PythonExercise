def Det(gems) :
    tempd={}
    s=0
    for i in gems :
        try :
            tempd[i]+=1
        except :
            tempd[i]=0
            s+=1



    return s


def solution(gems) :
    start=0
    end=0
    diclen=0
    dic={}
    for i in range(len(gems)) :
        try :
            dic[gems[i]]+=1
        except :
            dic[gems[i]]=1
            diclen+=1
    print('len',diclen)
    while start<=end :
        if end==len(gems) :
            break
        print(start,end)
        L=gems[start:end]
        if Det(L)>=diclen :
            if Det(L[start+1:end])>=diclen and len(L[start+1:end]) :
                start+=1
            else :
                break
        elif Det(L)<diclen :
            end+=1

    return[start,end]


l=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
l2=['XYZ','XYZ','XYZ']
print(solution(l))
print(solution(l2))

