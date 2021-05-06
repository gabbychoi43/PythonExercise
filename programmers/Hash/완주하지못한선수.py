def solution(participant, completion):

    Map={}

    for i in participant :
        try :
            Map[i]+=1
        except :
            Map[i]=1

    for i in completion :
        Map[i]-=1

    for i in Map :
        if Map[i]==1 :
            return i
