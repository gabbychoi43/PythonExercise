def solution(genres, plays):
    answer = []
    score={}
    for i in range(len(genres)) :
        try :
            score[genres[i]]+=plays[i]
        except :
            score[genres[i]]=plays[i]
    
    Musics={}
    for i in range(len(genres)) :
        try :
            Musics[genres[i]].append([i,plays[i]])
        except :
            Musics[genres[i]]=[[i,plays[i]]]
    for i,j in Musics.items() :
        j.sort(key=lambda x:x[0])
        j.sort(key=lambda x:x[1],reverse=True)
    
    L=list(score.keys())
    L.sort(key=lambda x:x[1],reverse=True)
    for i in L :
        answer.append(Musics[i][0][0])
        if len(Musics[i])>1 :
            answer.append(Musics[i][1][0])
        
            
    return answer