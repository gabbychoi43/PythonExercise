def solution(clothes):
    answer = 1
    D={}
    for i in clothes :
        
        x,y=i
        try :
            D[y]+=1
        except :
            D[y]=1
    for i in D :
        answer*=(D[i]+1)
        
    return answer-1